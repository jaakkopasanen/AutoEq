# Maximo iMetal iP-HS5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.1; 23 -8.0; 25 -7.9; 28 -7.7; 31 -7.5; 34 -7.4; 37 -7.2; 41 -7.0; 45 -6.8; 49 -6.7; 54 -6.5; 60 -6.4; 66 -6.2; 72 -6.1; 79 -5.9; 87 -5.7; 96 -5.5; 106 -5.2; 116 -5.0; 128 -4.7; 141 -4.5; 155 -4.2; 170 -3.9; 187 -3.5; 206 -3.1; 227 -2.6; 249 -2.2; 274 -1.7; 302 -1.2; 332 -0.7; 365 -0.5; 402 -0.2; 442 0.2; 486 0.5; 535 0.8; 588 1.0; 647 1.2; 712 1.4; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.6; 1526 -2.8; 1678 -3.4; 1846 -4.4; 2031 -5.3; 2234 -5.6; 2457 -4.8; 2703 -1.9; 2973 1.8; 3270 5.3; 3597 6.0; 3957 6.0; 4353 5.0; 4788 3.5; 5267 2.7; 5793 0.2; 6373 -5.6; 7010 -4.6; 7711 -1.3; 8482 0.0; 9330 -0.1; 10263 -1.8; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Maximo iMetal iP-HS5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Maximo iMetal iP-HS5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.29 | -7.8 dB |
| Peaking | 134 Hz   | 1.02 | -2.5 dB |
| Peaking | 2295 Hz  | 1.62 | -9.9 dB |
| Peaking | 3580 Hz  | 1.25 | 9.6 dB  |
| Peaking | 6630 Hz  | 4.58 | -8.6 dB |
| Peaking | 80 Hz    | 3.27 | -0.5 dB |
| Peaking | 231 Hz   | 2.25 | -0.8 dB |
| Peaking | 754 Hz   | 0.99 | 2.0 dB  |
| Peaking | 1319 Hz  | 2.13 | -1.8 dB |
| Peaking | 10386 Hz | 7.95 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Maximo%20iMetal%20iP-HS5/Maximo%20iMetal%20iP-HS5.png)