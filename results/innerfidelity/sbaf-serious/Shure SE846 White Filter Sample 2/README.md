# Shure SE846 White Filter Sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.4; 25 -2.4; 28 -2.4; 31 -2.4; 34 -2.4; 37 -2.4; 41 -2.3; 45 -2.3; 49 -2.3; 54 -2.3; 60 -2.3; 66 -2.3; 72 -2.3; 79 -2.4; 87 -2.4; 96 -2.5; 106 -2.4; 116 -2.2; 128 -2.1; 141 -2.0; 155 -1.9; 170 -1.7; 187 -1.5; 206 -1.3; 227 -1.0; 249 -0.8; 274 -0.6; 302 -0.4; 332 -0.2; 365 -0.1; 402 -0.0; 442 0.3; 486 0.2; 535 0.3; 588 0.7; 647 0.8; 712 0.8; 783 0.9; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.3; 1526 -1.9; 1678 -2.3; 1846 -2.4; 2031 -2.1; 2234 -1.4; 2457 0.8; 2703 3.3; 2973 5.9; 3270 6.0; 3597 6.0; 3957 5.3; 4353 3.1; 4788 3.6; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.6; 8482 -0.9; 9330 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.19 | -2.5 dB |
| Peaking | 719 Hz  | 0.6  | 1.5 dB  |
| Peaking | 2001 Hz | 1.1  | -4.9 dB |
| Peaking | 3187 Hz | 1.75 | 8.4 dB  |
| Peaking | 5798 Hz | 3.6  | 5.8 dB  |
| Peaking | 59 Hz   | 1.5  | 0.3 dB  |
| Peaking | 103 Hz  | 1.95 | -0.2 dB |
| Peaking | 6683 Hz | 7.64 | 2.1 dB  |
| Peaking | 7964 Hz | 3.8  | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20White%20Filter%20Sample%202/Shure%20SE846%20White%20Filter%20Sample%202.png)