# Polk Audio UltraFit 2000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 4.7; 79 3.6; 87 2.5; 96 1.4; 106 0.9; 116 0.6; 128 0.4; 141 0.4; 155 0.5; 170 0.8; 187 1.2; 206 1.5; 227 1.9; 249 2.3; 274 2.8; 302 3.3; 332 4.3; 365 4.6; 402 5.2; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 5.5; 947 1.9; 1042 -1.1; 1146 -2.0; 1261 -2.7; 1387 -3.1; 1526 -3.2; 1678 -3.5; 1846 -3.9; 2031 -3.6; 2234 -2.5; 2457 -0.2; 2703 1.7; 2973 3.4; 3270 3.6; 3597 2.5; 3957 2.1; 4353 3.3; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -4.1; 9330 -5.0; 10263 -1.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB   |
| Peaking | 665 Hz  | 0.76 | 8.8 dB   |
| Peaking | 1429 Hz | 0.94 | -8.0 dB  |
| Peaking | 5948 Hz | 0.77 | 7.7 dB   |
| Peaking | 8824 Hz | 2.36 | -10.1 dB |
| Peaking | 66 Hz   | 3.61 | 2.1 dB   |
| Peaking | 121 Hz  | 1.71 | -1.6 dB  |
| Peaking | 2158 Hz | 3.34 | -2.9 dB  |
| Peaking | 3158 Hz | 1.38 | 3.4 dB   |
| Peaking | 3927 Hz | 3.4  | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)