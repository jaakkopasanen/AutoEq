# Polk Audio UltraFit 3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.3; 23 -9.3; 25 -9.3; 28 -9.4; 31 -9.4; 34 -9.5; 37 -9.5; 41 -9.6; 45 -9.6; 49 -9.7; 54 -9.8; 60 -10.0; 66 -10.2; 72 -10.3; 79 -10.5; 87 -10.7; 96 -10.9; 106 -10.9; 116 -10.8; 128 -10.8; 141 -10.7; 155 -10.6; 170 -10.3; 187 -9.9; 206 -9.6; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.8; 365 -6.1; 402 -5.4; 442 -4.6; 486 -4.0; 535 -3.3; 588 -2.2; 647 -1.5; 712 -1.0; 783 -0.5; 861 -0.4; 947 -0.3; 1042 0.3; 1146 0.4; 1261 0.4; 1387 0.1; 1526 -0.3; 1678 -0.5; 1846 -0.2; 2031 0.3; 2234 1.0; 2457 2.6; 2703 4.0; 2973 5.9; 3270 6.0; 3597 6.0; 3957 5.9; 4353 2.9; 4788 0.8; 5267 3.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.21 | -8.8 dB |
| Peaking | 143 Hz  | 0.63 | -6.3 dB |
| Peaking | 306 Hz  | 1.08 | -3.3 dB |
| Peaking | 3327 Hz | 2.19 | 6.7 dB  |
| Peaking | 6080 Hz | 4.63 | 6.0 dB  |
| Peaking | 1108 Hz | 0.93 | 3.6 dB  |
| Peaking | 1541 Hz | 0.52 | -3.3 dB |
| Peaking | 3115 Hz | 1.72 | 3.4 dB  |
| Peaking | 3298 Hz | 6.12 | -2.9 dB |
| Peaking | 8246 Hz | 5.46 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)