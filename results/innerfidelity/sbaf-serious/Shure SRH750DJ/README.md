# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.5; 41 4.8; 45 4.2; 49 3.7; 54 3.3; 60 2.8; 66 2.1; 72 1.5; 79 0.8; 87 0.4; 96 0.4; 106 0.8; 116 0.8; 128 0.0; 141 -0.6; 155 -1.1; 170 -0.7; 187 -0.8; 206 -1.2; 227 -1.1; 249 -2.5; 274 -2.6; 302 -2.2; 332 -1.7; 365 -1.5; 402 -1.7; 442 -1.9; 486 -2.1; 535 -2.0; 588 -1.7; 647 -1.3; 712 -0.9; 783 -0.2; 861 0.2; 947 0.4; 1042 -0.2; 1146 -0.3; 1261 -0.1; 1387 -0.7; 1526 -1.9; 1678 -3.4; 1846 -5.5; 2031 -7.2; 2234 -7.9; 2457 -6.0; 2703 -3.8; 2973 -0.8; 3270 1.0; 3597 2.3; 3957 1.9; 4353 -1.2; 4788 1.7; 5267 5.0; 5793 5.6; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -4.5; 9330 -5.6; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.7  | 6.4 dB  |
| Peaking | 304 Hz  | 0.79 | -2.3 dB |
| Peaking | 2160 Hz | 2.93 | -8.7 dB |
| Peaking | 6003 Hz | 2.13 | 6.5 dB  |
| Peaking | 8920 Hz | 4.46 | -7.8 dB |
| Peaking | 563 Hz  | 3.36 | -1.0 dB |
| Peaking | 922 Hz  | 2.58 | 1.1 dB  |
| Peaking | 2607 Hz | 5.36 | -1.8 dB |
| Peaking | 3653 Hz | 2.55 | 2.8 dB  |
| Peaking | 4413 Hz | 7.84 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)