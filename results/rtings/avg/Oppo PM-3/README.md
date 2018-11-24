# Oppo PM-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -1.5; 23 -1.3; 25 -1.1; 28 -0.8; 31 -0.5; 34 -0.2; 37 -0.0; 41 0.2; 45 0.2; 49 0.3; 54 0.1; 60 -0.2; 66 -0.8; 72 -1.4; 79 -2.0; 87 -2.6; 96 -3.1; 106 -3.5; 116 -3.9; 128 -4.2; 141 -4.4; 155 -4.5; 170 -4.3; 187 -4.0; 206 -3.6; 227 -3.1; 249 -2.5; 274 -2.0; 302 -1.4; 332 -1.0; 365 -0.8; 402 -1.0; 442 -1.3; 486 -1.8; 535 -2.4; 588 -3.0; 647 -2.9; 712 -2.5; 783 -1.9; 861 -1.1; 947 -0.3; 1042 -0.1; 1146 -1.1; 1261 -2.0; 1387 -2.5; 1526 -3.0; 1678 -3.4; 1846 -4.4; 2031 -4.3; 2234 -5.0; 2457 -4.6; 2703 -4.5; 2973 -4.2; 3270 -3.7; 3597 -3.3; 3957 -2.8; 4353 -3.3; 4788 -1.7; 5267 0.1; 5793 0.7; 6373 -3.4; 7010 -7.9; 7711 -8.3; 8482 -9.3; 9330 -9.3; 10263 -4.6; 11289 -0.1; 12418 -0.4; 13660 -2.8; 15026 -1.1; 16529 0.0; 18182 0.0; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 0.97 | -4.7 dB  |
| Peaking | 616 Hz   | 3.05 | -2.7 dB  |
| Peaking | 2335 Hz  | 1.15 | -4.9 dB  |
| Peaking | 8459 Hz  | 2.53 | -10.4 dB |
| Peaking | 14058 Hz | 6.8  | -2.2 dB  |
| Peaking | 23 Hz    | 2.29 | -1.5 dB  |
| Peaking | 1006 Hz  | 5.63 | 1.2 dB   |
| Peaking | 5838 Hz  | 5.15 | 5.3 dB   |
| Peaking | 6712 Hz  | 3.52 | -3.5 dB  |
| Peaking | 10683 Hz | 3.45 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Oppo%20PM-3/Oppo%20PM-3.png)