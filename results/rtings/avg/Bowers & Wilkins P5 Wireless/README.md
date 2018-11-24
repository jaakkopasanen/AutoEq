# Bowers & Wilkins P5 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.8; 28 -3.9; 31 -3.9; 34 -3.8; 37 -3.6; 41 -3.4; 45 -3.3; 49 -3.3; 54 -3.2; 60 -3.2; 66 -3.3; 72 -3.2; 79 -3.2; 87 -3.1; 96 -3.1; 106 -3.2; 116 -3.1; 128 -3.0; 141 -2.8; 155 -2.6; 170 -2.6; 187 -2.4; 206 -2.2; 227 -2.1; 249 -2.0; 274 -1.7; 302 -1.2; 332 -0.6; 365 0.5; 402 1.4; 442 2.0; 486 2.4; 535 2.5; 588 2.6; 647 2.4; 712 2.2; 783 1.7; 861 1.2; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.6; 1526 -3.7; 1678 -4.3; 1846 -3.5; 2031 -0.9; 2234 1.0; 2457 1.4; 2703 1.8; 2973 1.9; 3270 1.6; 3597 1.3; 3957 0.1; 4353 -1.2; 4788 -1.1; 5267 -0.2; 5793 0.0; 6373 -0.3; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -4.8; 18182 -8.9; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.07 | -3.4 dB  |
| Peaking | 549 Hz   | 1.02 | 5.0 dB   |
| Peaking | 1698 Hz  | 2    | -5.6 dB  |
| Peaking | 2454 Hz  | 1.79 | 3.4 dB   |
| Peaking | 18407 Hz | 2.03 | -10.0 dB |
| Peaking | 812 Hz   | 0.51 | -0.2 dB  |
| Peaking | 3659 Hz  | 2.75 | 1.5 dB   |
| Peaking | 4386 Hz  | 3.37 | -2.3 dB  |
| Peaking | 6986 Hz  | 9.77 | 2.5 dB   |
| Peaking | 14496 Hz | 3.58 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Wireless/Bowers%20&%20Wilkins%20P5%20Wireless.png)