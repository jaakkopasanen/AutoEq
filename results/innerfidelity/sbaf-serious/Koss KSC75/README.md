# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.3; 49 4.3; 54 3.2; 60 2.0; 66 0.9; 72 -0.0; 79 -0.9; 87 -1.8; 96 -2.5; 106 -3.0; 116 -3.2; 128 -3.4; 141 -3.4; 155 -3.5; 170 -3.2; 187 -3.0; 206 -2.9; 227 -2.7; 249 -2.5; 274 -2.1; 302 -1.8; 332 -1.5; 365 -1.2; 402 -0.9; 442 -0.5; 486 -0.4; 535 -0.3; 588 0.2; 647 0.2; 712 0.2; 783 0.5; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.5; 1387 -1.4; 1526 -2.5; 1678 -3.3; 1846 -4.3; 2031 -4.9; 2234 -5.7; 2457 -5.5; 2703 -4.2; 2973 -2.9; 3270 -2.9; 3597 5.1; 3957 5.4; 4353 -4.3; 4788 -9.3; 5267 -2.8; 5793 1.4; 6373 1.7; 7010 1.8; 7711 -0.1; 8482 -3.9; 9330 -6.6; 10263 -4.9; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.56 | 7.5 dB   |
| Peaking | 2739 Hz | 0.96 | -15.6 dB |
| Peaking | 3976 Hz | 1.13 | 23.0 dB  |
| Peaking | 4651 Hz | 3.74 | -21.1 dB |
| Peaking | 9407 Hz | 3.24 | -9.7 dB  |
| Peaking | 50 Hz   | 1.74 | 3.5 dB   |
| Peaking | 136 Hz  | 0.55 | -3.9 dB  |
| Peaking | 907 Hz  | 0.81 | 1.4 dB   |
| Peaking | 1824 Hz | 2.84 | -1.5 dB  |
| Peaking | 5367 Hz | 6.64 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)