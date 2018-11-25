# Bang & Olufsen Beoplay H9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -13.5; 23 -13.3; 25 -13.2; 28 -12.8; 31 -12.4; 34 -11.9; 37 -11.4; 41 -10.7; 45 -10.1; 49 -9.6; 54 -9.2; 60 -8.8; 66 -8.4; 72 -8.1; 79 -7.7; 87 -7.3; 96 -7.0; 106 -6.8; 116 -6.6; 128 -6.5; 141 -6.3; 155 -6.1; 170 -5.8; 187 -5.5; 206 -5.1; 227 -4.4; 249 -3.7; 274 -2.9; 302 -2.3; 332 -1.5; 365 -0.7; 402 -0.0; 442 0.7; 486 1.4; 535 1.8; 588 2.1; 647 2.4; 712 2.6; 783 2.3; 861 1.6; 947 0.6; 1042 -0.3; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.2; 1678 -3.6; 1846 -3.6; 2031 -4.6; 2234 -5.8; 2457 -6.6; 2703 -4.9; 2973 -4.4; 3270 -6.3; 3597 -6.6; 3957 -5.0; 4353 -3.8; 4788 -2.4; 5267 0.1; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -6.3; 9330 -10.8; 10263 -10.3; 11289 -7.3; 12418 -4.2; 13660 -2.1; 15026 -0.1; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.27 | -13.3 dB |
| Peaking | 162 Hz   | 1.36 | -3.6 dB  |
| Peaking | 2277 Hz  | 2.21 | -6.0 dB  |
| Peaking | 3553 Hz  | 4.2  | -6.0 dB  |
| Peaking | 10051 Hz | 3.48 | -12.3 dB |
| Peaking | 645 Hz   | 1.26 | 4.4 dB   |
| Peaking | 1157 Hz  | 0.19 | -1.2 dB  |
| Peaking | 6307 Hz  | 3.67 | 8.3 dB   |
| Peaking | 8947 Hz  | 9.37 | -4.4 dB  |
| Peaking | 12055 Hz | 4.95 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H9/Bang%20&%20Olufsen%20Beoplay%20H9.png)