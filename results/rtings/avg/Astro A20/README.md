# Astro A20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 0.0; 23 1.2; 25 0.7; 28 -0.0; 31 -0.7; 34 -1.3; 37 -1.8; 41 -2.4; 45 -3.0; 49 -3.4; 54 -3.9; 60 -4.4; 66 -4.8; 72 -5.1; 79 -5.3; 87 -5.6; 96 -5.7; 106 -5.7; 116 -5.7; 128 -5.6; 141 -5.3; 155 -4.8; 170 -4.5; 187 -4.0; 206 -3.3; 227 -2.7; 249 -2.0; 274 -1.7; 302 -2.0; 332 -0.7; 365 0.5; 402 1.0; 442 0.1; 486 -0.4; 535 -1.2; 588 -1.6; 647 -1.2; 712 -0.4; 783 -0.7; 861 -0.4; 947 -0.2; 1042 0.3; 1146 1.0; 1261 1.6; 1387 1.8; 1526 1.9; 1678 1.8; 1846 1.6; 2031 1.7; 2234 2.0; 2457 2.1; 2703 0.9; 2973 -1.7; 3270 -3.7; 3597 -4.8; 3957 -6.1; 4353 -5.1; 4788 -5.3; 5267 -9.6; 5793 -9.5; 6373 -9.4; 7010 -8.4; 7711 -6.9; 8482 -7.4; 9330 -5.7; 10263 -0.3; 11289 0.0; 12418 -3.7; 13660 -6.4; 15026 -5.4; 16529 -5.2; 18182 -5.7; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 75 Hz    | 0.94 | -4.4 dB |
| Peaking | 146 Hz   | 1.14 | -3.8 dB |
| Peaking | 5766 Hz  | 1.76 | -9.7 dB |
| Peaking | 8415 Hz  | 4.42 | -4.0 dB |
| Peaking | 17371 Hz | 0.81 | -6.1 dB |
| Peaking | 22 Hz    | 2.26 | 2.1 dB  |
| Peaking | 1456 Hz  | 2.69 | 2.1 dB  |
| Peaking | 2430 Hz  | 2.24 | 3.8 dB  |
| Peaking | 3658 Hz  | 2.01 | -3.8 dB |
| Peaking | 4586 Hz  | 6.7  | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A20/Astro%20A20.png)