# Skullcandy Jib

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.7; 28 -5.0; 31 -5.2; 34 -5.4; 37 -5.6; 41 -5.7; 45 -5.9; 49 -5.9; 54 -6.0; 60 -6.3; 66 -6.5; 72 -6.5; 79 -6.6; 87 -6.7; 96 -7.0; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.2; 155 -8.2; 170 -8.1; 187 -8.1; 206 -7.8; 227 -7.4; 249 -6.8; 274 -6.1; 302 -5.4; 332 -4.7; 365 -4.1; 402 -3.5; 442 -2.9; 486 -2.1; 535 -1.5; 588 -0.7; 647 0.1; 712 0.8; 783 1.2; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.0; 1261 -1.4; 1387 -1.9; 1526 -2.3; 1678 -2.5; 1846 -2.3; 2031 -2.0; 2234 -1.7; 2457 -1.4; 2703 -1.7; 2973 -1.7; 3270 -0.4; 3597 0.8; 3957 0.4; 4353 -0.5; 4788 0.0; 5267 0.9; 5793 1.5; 6373 -0.2; 7010 1.2; 7711 0.3; 8482 0.0; 9330 -1.6; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.37 | -5.5 dB |
| Peaking | 157 Hz  | 0.98 | -5.2 dB |
| Peaking | 274 Hz  | 1.45 | -3.1 dB |
| Peaking | 1708 Hz | 2.67 | -2.6 dB |
| Peaking | 2728 Hz | 4.65 | -1.5 dB |
| Peaking | 425 Hz  | 3.7  | -0.8 dB |
| Peaking | 778 Hz  | 3.13 | 2.1 dB  |
| Peaking | 5570 Hz | 7.36 | 1.4 dB  |
| Peaking | 7396 Hz | 2.97 | 0.7 dB  |
| Peaking | 9545 Hz | 7.21 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Jib/Skullcandy%20Jib.png)