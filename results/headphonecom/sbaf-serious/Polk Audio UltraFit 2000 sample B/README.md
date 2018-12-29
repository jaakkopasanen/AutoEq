# Polk Audio UltraFit 2000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 4.7; 66 3.4; 72 2.2; 79 1.2; 87 0.2; 96 -0.4; 106 -1.0; 116 -1.3; 128 -1.6; 141 -1.7; 155 -1.6; 170 -1.5; 187 -1.1; 206 -0.8; 227 -0.5; 249 -0.1; 274 0.3; 302 1.1; 332 2.4; 365 2.6; 402 3.4; 442 4.3; 486 4.5; 535 4.9; 588 5.5; 647 5.8; 712 5.9; 783 5.3; 861 3.8; 947 1.2; 1042 -0.9; 1146 -2.5; 1261 -3.2; 1387 -3.8; 1526 -4.3; 1678 -4.6; 1846 -4.9; 2031 -4.3; 2234 -2.8; 2457 -0.2; 2703 2.0; 2973 3.7; 3270 4.1; 3597 3.3; 3957 2.3; 4353 3.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.7; 9330 -6.0; 10263 -2.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.05 | 7.3 dB   |
| Peaking | 663 Hz  | 1.3  | 7.6 dB   |
| Peaking | 1625 Hz | 1.05 | -7.9 dB  |
| Peaking | 5213 Hz | 0.6  | 7.2 dB   |
| Peaking | 9108 Hz | 2.68 | -10.3 dB |
| Peaking | 58 Hz   | 2.58 | 3.2 dB   |
| Peaking | 136 Hz  | 0.7  | -2.5 dB  |
| Peaking | 377 Hz  | 2.25 | 1.8 dB   |
| Peaking | 3025 Hz | 5.22 | 2.3 dB   |
| Peaking | 3984 Hz | 7.05 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20B/Polk%20Audio%20UltraFit%202000%20sample%20B.png)