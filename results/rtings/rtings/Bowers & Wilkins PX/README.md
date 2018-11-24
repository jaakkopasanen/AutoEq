# Bowers & Wilkins PX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.9; 23 -4.1; 25 -4.3; 28 -4.7; 31 -4.9; 34 -5.0; 37 -5.1; 41 -5.0; 45 -5.0; 49 -5.0; 54 -5.0; 60 -5.1; 66 -5.4; 72 -5.7; 79 -6.1; 87 -6.6; 96 -7.1; 106 -7.6; 116 -8.0; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.3; 187 -8.5; 206 -8.8; 227 -9.5; 249 -10.0; 274 -10.3; 302 -10.1; 332 -9.4; 365 -8.5; 402 -7.5; 442 -6.6; 486 -5.9; 535 -5.2; 588 -4.4; 647 -3.4; 712 -2.4; 783 -1.3; 861 -0.5; 947 -0.1; 1042 -0.2; 1146 -1.1; 1261 -1.5; 1387 -1.5; 1526 -1.7; 1678 -2.3; 1846 -2.6; 2031 -3.4; 2234 -3.7; 2457 -3.6; 2703 -1.4; 2973 3.6; 3270 5.7; 3597 -4.2; 3957 -3.9; 4353 -3.0; 4788 -0.9; 5267 2.8; 5793 3.9; 6373 0.9; 7010 -0.3; 7711 0.2; 8482 -2.8; 9330 -4.9; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 -3.0; 15026 -1.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.61 | -4.1 dB |
| Peaking | 122 Hz   | 0.73 | -5.7 dB |
| Peaking | 306 Hz   | 0.93 | -8.3 dB |
| Peaking | 2125 Hz  | 3.42 | -3.9 dB |
| Peaking | 14011 Hz | 3.68 | -3.0 dB |
| Peaking | 925 Hz   | 4.85 | 1.8 dB  |
| Peaking | 3192 Hz  | 5.56 | 13.6 dB |
| Peaking | 3625 Hz  | 2.04 | -8.2 dB |
| Peaking | 5569 Hz  | 4.32 | 6.0 dB  |
| Peaking | 9118 Hz  | 7.49 | -5.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bowers%20&%20Wilkins%20PX/Bowers%20&%20Wilkins%20PX.png)