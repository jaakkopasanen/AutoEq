# Jays v-JAYS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.5; 45 3.1; 49 1.9; 54 0.5; 60 -0.8; 66 -1.7; 72 -2.3; 79 -2.8; 87 -3.0; 96 -3.0; 106 -2.7; 116 -2.4; 128 -2.2; 141 -1.8; 155 -1.6; 170 -1.1; 187 -0.8; 206 -0.5; 227 0.0; 249 0.6; 274 1.0; 302 0.7; 332 -1.8; 365 -1.4; 402 -0.7; 442 -0.1; 486 -0.0; 535 0.2; 588 0.6; 647 0.7; 712 0.5; 783 0.6; 861 0.2; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.6; 1387 -2.9; 1526 -4.6; 1678 -6.3; 1846 -7.7; 2031 -8.2; 2234 -8.3; 2457 -7.9; 2703 -8.3; 2973 -8.9; 3270 -8.8; 3597 -10.6; 3957 -12.6; 4353 -10.7; 4788 -7.2; 5267 -4.6; 5793 -2.2; 6373 2.9; 7010 0.1; 7711 -3.1; 8482 -5.6; 9330 -6.1; 10263 -1.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.8; 16529 -7.0; 18182 -8.6; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays v-JAYS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays v-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 1.91 | 7.3 dB   |
| Peaking | 2144 Hz  | 1.61 | -7.7 dB  |
| Peaking | 3950 Hz  | 2.37 | -11.4 dB |
| Peaking | 17003 Hz | 2.61 | -4.9 dB  |
| Peaking | 18647 Hz | 1.67 | -6.7 dB  |
| Peaking | 23 Hz    | 0.06 | 1.8 dB   |
| Peaking | 97 Hz    | 0.8  | -5.0 dB  |
| Peaking | 6528 Hz  | 5.81 | 6.9 dB   |
| Peaking | 9269 Hz  | 2.07 | -8.9 dB  |
| Peaking | 10729 Hz | 1.69 | 5.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20v-JAYS/Jays%20v-JAYS.png)