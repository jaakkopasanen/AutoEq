# Skullcandy Grind

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -2.8; 23 -3.3; 25 -3.7; 28 -4.3; 31 -4.7; 34 -4.9; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.4; 54 -5.5; 60 -5.7; 66 -5.9; 72 -6.0; 79 -6.1; 87 -6.1; 96 -6.2; 106 -6.3; 116 -6.3; 128 -6.3; 141 -6.2; 155 -6.1; 170 -6.1; 187 -5.9; 206 -5.9; 227 -5.8; 249 -5.7; 274 -5.8; 302 -6.0; 332 -5.4; 365 -4.9; 402 -4.3; 442 -3.7; 486 -3.2; 535 -2.5; 588 -1.8; 647 -0.7; 712 0.4; 783 1.4; 861 1.8; 947 1.1; 1042 -1.1; 1146 -3.4; 1261 -2.5; 1387 -4.3; 1526 -4.8; 1678 -5.1; 1846 -7.4; 2031 -9.4; 2234 -9.7; 2457 -8.9; 2703 -7.8; 2973 -6.8; 3270 -5.7; 3597 -4.6; 3957 -6.3; 4353 -4.4; 4788 -2.3; 5267 -0.4; 5793 -0.9; 6373 -5.0; 7010 -8.1; 7711 -9.3; 8482 -9.6; 9330 -8.4; 10263 -3.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.0; 18182 -5.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.41 | -5.3 dB  |
| Peaking | 165 Hz   | 0.94 | -3.4 dB  |
| Peaking | 324 Hz   | 1.79 | -3.8 dB  |
| Peaking | 2317 Hz  | 1.38 | -9.7 dB  |
| Peaking | 8200 Hz  | 2.44 | -10.3 dB |
| Peaking | 846 Hz   | 4.09 | 3.8 dB   |
| Peaking | 5475 Hz  | 5.16 | 4.8 dB   |
| Peaking | 9481 Hz  | 0.47 | -3.9 dB  |
| Peaking | 12771 Hz | 0.73 | 6.1 dB   |
| Peaking | 19170 Hz | 1.04 | -7.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Grind/Skullcandy%20Grind.png)