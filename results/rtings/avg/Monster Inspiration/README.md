# Monster Inspiration

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 -0.2; 25 -1.2; 28 -2.6; 31 -3.8; 34 -4.8; 37 -5.6; 41 -6.6; 45 -7.5; 49 -8.3; 54 -9.1; 60 -9.9; 66 -10.6; 72 -11.2; 79 -11.7; 87 -12.1; 96 -12.4; 106 -12.7; 116 -12.8; 128 -12.7; 141 -12.5; 155 -12.2; 170 -11.6; 187 -10.9; 206 -10.0; 227 -9.0; 249 -8.0; 274 -6.9; 302 -5.5; 332 -3.8; 365 -1.9; 402 -0.8; 442 -0.0; 486 1.9; 535 3.6; 588 4.0; 647 3.7; 712 2.9; 783 2.1; 861 1.4; 947 0.6; 1042 -0.3; 1146 -1.2; 1261 -2.4; 1387 -3.7; 1526 -4.6; 1678 -5.7; 1846 -7.2; 2031 -8.5; 2234 -9.7; 2457 -10.9; 2703 -12.5; 2973 -12.4; 3270 -12.0; 3597 -10.7; 3957 -8.8; 4353 -7.7; 4788 -9.2; 5267 -8.9; 5793 -4.3; 6373 2.4; 7010 -1.8; 7711 -7.1; 8482 -8.7; 9330 -6.4; 10263 -4.7; 11289 -6.3; 12418 -10.3; 13660 -13.4; 15026 -13.5; 16529 -12.0; 18182 -7.9; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.74 | -11.1 dB |
| Peaking | 172 Hz   | 1.36 | -8.0 dB  |
| Peaking | 2437 Hz  | 1.68 | -7.9 dB  |
| Peaking | 3560 Hz  | 1.39 | -7.7 dB  |
| Peaking | 14982 Hz | 0.92 | -14.2 dB |
| Peaking | 21 Hz    | 3.03 | 2.1 dB   |
| Peaking | 610 Hz   | 2.21 | 5.8 dB   |
| Peaking | 5428 Hz  | 4.47 | -7.3 dB  |
| Peaking | 6273 Hz  | 4.03 | 9.7 dB   |
| Peaking | 8132 Hz  | 5.35 | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monster%20Inspiration/Monster%20Inspiration.png)