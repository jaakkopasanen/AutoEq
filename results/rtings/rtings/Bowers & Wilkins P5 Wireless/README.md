# Bowers & Wilkins P5 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.8; 28 -3.9; 31 -3.9; 34 -3.8; 37 -3.6; 41 -3.4; 45 -3.3; 49 -3.3; 54 -3.2; 60 -3.2; 66 -3.3; 72 -3.2; 79 -3.2; 87 -3.1; 96 -3.1; 106 -3.2; 116 -3.1; 128 -3.0; 141 -2.8; 155 -2.6; 170 -2.6; 187 -2.4; 206 -2.2; 227 -2.1; 249 -2.0; 274 -1.7; 302 -1.2; 332 -0.6; 365 0.5; 402 1.4; 442 2.0; 486 2.4; 535 2.5; 588 2.6; 647 2.4; 712 2.2; 783 1.7; 861 1.2; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.6; 1526 -3.7; 1678 -4.3; 1846 -3.5; 2031 -0.9; 2234 0.9; 2457 1.4; 2703 2.1; 2973 2.4; 3270 2.3; 3597 2.3; 3957 1.3; 4353 0.1; 4788 0.6; 5267 2.3; 5793 2.5; 6373 0.9; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.8; 18182 -4.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.05 | -3.4 dB |
| Peaking | 530 Hz   | 1.04 | 4.8 dB  |
| Peaking | 1652 Hz  | 1.76 | -7.7 dB |
| Peaking | 2347 Hz  | 0.66 | 4.1 dB  |
| Peaking | 17942 Hz | 2.84 | -5.2 dB |
| Peaking | 768 Hz   | 3.24 | 0.5 dB  |
| Peaking | 4495 Hz  | 3.81 | -3.5 dB |
| Peaking | 5239 Hz  | 1.48 | 2.2 dB  |
| Peaking | 8580 Hz  | 2.85 | -0.9 dB |
| Peaking | 15472 Hz | 6.34 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bowers%20&%20Wilkins%20P5%20Wireless/Bowers%20&%20Wilkins%20P5%20Wireless.png)