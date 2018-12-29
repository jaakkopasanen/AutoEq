# Fidue A31s
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.8; 23 -7.9; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -8.9; 54 -8.9; 60 -9.0; 66 -9.1; 72 -9.1; 79 -9.2; 87 -9.3; 96 -9.4; 106 -9.1; 116 -9.0; 128 -8.8; 141 -8.6; 155 -8.3; 170 -8.0; 187 -7.5; 206 -7.0; 227 -6.5; 249 -5.9; 274 -5.3; 302 -4.7; 332 -4.0; 365 -3.4; 402 -2.8; 442 -2.0; 486 -1.6; 535 -1.0; 588 -0.2; 647 0.2; 712 0.4; 783 1.0; 861 0.6; 947 0.3; 1042 0.3; 1146 -0.2; 1261 -0.9; 1387 -1.5; 1526 -1.7; 1678 -3.0; 1846 -4.3; 2031 -5.0; 2234 -5.6; 2457 -4.2; 2703 -1.8; 2973 1.4; 3270 3.2; 3597 3.2; 3957 0.4; 4353 -4.3; 4788 -1.4; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A31s GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A31s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.29 | -8.5 dB |
| Peaking | 167 Hz  | 0.75 | -4.4 dB |
| Peaking | 2170 Hz | 2.29 | -6.0 dB |
| Peaking | 3270 Hz | 5.42 | 5.1 dB  |
| Peaking | 5964 Hz | 4.6  | 7.2 dB  |
| Peaking | 323 Hz  | 2.38 | -0.8 dB |
| Peaking | 767 Hz  | 1.92 | 1.8 dB  |
| Peaking | 3744 Hz | 6.64 | 3.0 dB  |
| Peaking | 4448 Hz | 4.87 | -6.3 dB |
| Peaking | 5228 Hz | 8.32 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A31s/Fidue%20A31s.png)