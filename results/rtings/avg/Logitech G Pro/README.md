# Logitech G Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -3.9; 23 -4.3; 25 -4.7; 28 -5.2; 31 -5.5; 34 -5.7; 37 -5.8; 41 -5.8; 45 -5.9; 49 -5.9; 54 -5.9; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.4; 87 -6.7; 96 -7.2; 106 -8.0; 116 -8.7; 128 -9.2; 141 -9.3; 155 -9.3; 170 -9.2; 187 -8.7; 206 -8.0; 227 -7.1; 249 -5.9; 274 -4.4; 302 -2.9; 332 -1.7; 365 -1.4; 402 -1.7; 442 -2.5; 486 -3.4; 535 -3.9; 588 -4.0; 647 -3.7; 712 -2.8; 783 -1.7; 861 -0.8; 947 -0.2; 1042 -0.0; 1146 -0.3; 1261 -0.9; 1387 -2.3; 1526 -3.2; 1678 -3.3; 1846 -3.0; 2031 -3.0; 2234 -2.6; 2457 -2.8; 2703 -2.6; 2973 -1.0; 3270 -0.4; 3597 -3.8; 3957 -4.6; 4353 -4.3; 4788 -4.4; 5267 0.1; 5793 -0.2; 6373 -0.0; 7010 -3.0; 7711 -5.5; 8482 -7.1; 9330 -7.0; 10263 -4.7; 11289 -2.6; 12418 -2.6; 13660 -3.8; 15026 -5.0; 16529 -4.6; 18182 -5.7; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.35 | -5.3 dB |
| Peaking | 161 Hz   | 1.06 | -7.7 dB |
| Peaking | 590 Hz   | 3.24 | -3.5 dB |
| Peaking | 1854 Hz  | 1.81 | -2.7 dB |
| Peaking | 19359 Hz | 0.11 | -5.2 dB |
| Peaking | 344 Hz   | 6.25 | 1.6 dB  |
| Peaking | 4467 Hz  | 2.55 | -6.5 dB |
| Peaking | 5756 Hz  | 1.39 | 7.9 dB  |
| Peaking | 8583 Hz  | 1.39 | -6.8 dB |
| Peaking | 11558 Hz | 2.15 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G%20Pro/Logitech%20G%20Pro.png)