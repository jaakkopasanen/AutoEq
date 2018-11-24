# Polk Audio UltraFit 2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.2; 66 3.9; 72 2.7; 79 1.6; 87 0.5; 96 -0.4; 106 -0.9; 116 -1.1; 128 -1.2; 141 -1.2; 155 -1.0; 170 -0.7; 187 -0.3; 206 0.1; 227 0.5; 249 1.0; 274 1.5; 302 2.1; 332 2.6; 365 3.1; 402 3.7; 442 4.5; 486 4.9; 535 5.6; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 3.8; 947 1.1; 1042 -0.5; 1146 -1.1; 1261 -1.8; 1387 -2.1; 1526 -2.7; 1678 -2.9; 1846 -2.6; 2031 -1.5; 2234 0.2; 2457 2.4; 2703 4.2; 2973 5.7; 3270 5.5; 3597 3.9; 3957 3.6; 4353 4.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -1.8; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.68 | 7.6 dB   |
| Peaking | 579 Hz  | 0.51 | 18.8 dB  |
| Peaking | 913 Hz  | 0.15 | -12.8 dB |
| Peaking | 2960 Hz | 1.98 | 9.9 dB   |
| Peaking | 5334 Hz | 1.37 | 11.2 dB  |
| Peaking | 60 Hz   | 4.42 | 1.7 dB   |
| Peaking | 107 Hz  | 2.69 | -1.3 dB  |
| Peaking | 801 Hz  | 3.71 | 4.7 dB   |
| Peaking | 839 Hz  | 1.53 | -2.5 dB  |
| Peaking | 8932 Hz | 7.93 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)