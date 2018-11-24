# Polk Audio UltraFit 2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 4.2; 66 3.0; 72 1.8; 79 0.7; 87 -0.2; 96 -1.0; 106 -1.5; 116 -1.7; 128 -2.0; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.5; 206 -1.2; 227 -0.8; 249 -0.4; 274 -0.0; 302 0.8; 332 1.7; 365 2.1; 402 2.9; 442 3.4; 486 3.8; 535 4.2; 588 4.8; 647 5.1; 712 5.1; 783 4.4; 861 2.9; 947 0.7; 1042 -0.4; 1146 -1.7; 1261 -2.2; 1387 -2.4; 1526 -3.4; 1678 -3.6; 1846 -3.1; 2031 -1.9; 2234 -0.0; 2457 2.5; 2703 4.6; 2973 5.9; 3270 5.9; 3597 4.7; 3957 4.2; 4353 5.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -2.7; 10263 -0.3; 11289 0.0
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
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 37 Hz    |  0.65 | 7.9 dB   |
| Peaking | 577 Hz   |  0.51 | 17.7 dB  |
| Peaking | 872 Hz   |  0.13 | -12.9 dB |
| Peaking | 2979 Hz  |  1.95 | 10.4 dB  |
| Peaking | 5281 Hz  |  1.31 | 11.6 dB  |
| Peaking | 790 Hz   |  2.66 | 4.0 dB   |
| Peaking | 814 Hz   |  1.19 | -2.3 dB  |
| Peaking | 6452 Hz  | 10.07 | 1.6 dB   |
| Peaking | 9177 Hz  |  4.43 | -3.1 dB  |
| Peaking | 11596 Hz |  1.4  | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)