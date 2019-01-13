# Focal Listen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.3; 28 1.1; 31 1.0; 34 1.0; 37 1.0; 41 1.1; 45 1.3; 49 1.5; 54 1.9; 60 2.5; 66 3.1; 72 3.7; 79 4.4; 87 4.9; 96 5.2; 106 5.0; 116 4.2; 128 2.7; 141 1.6; 155 1.1; 170 0.7; 187 -0.9; 206 -1.5; 227 -1.8; 249 -2.0; 274 -2.1; 302 -2.0; 332 -1.9; 365 -1.5; 402 -1.3; 442 -1.0; 486 -1.2; 535 -1.2; 588 -0.7; 647 -0.6; 712 -0.5; 783 0.0; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.0; 1387 -0.4; 1526 -0.9; 1678 -1.2; 1846 -1.1; 2031 -0.5; 2234 0.5; 2457 2.0; 2703 3.2; 2973 5.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.1; 4788 1.3; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -1.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Listen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Listen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 17 Hz   |  1.45 | 1.8 dB  |
| Peaking | 97 Hz   |  1.13 | 6.0 dB  |
| Peaking | 245 Hz  |  0.78 | -2.9 dB |
| Peaking | 3424 Hz |  2.59 | 6.7 dB  |
| Peaking | 5915 Hz |  4.03 | 6.1 dB  |
| Peaking | 867 Hz  |  5.7  | 0.9 dB  |
| Peaking | 1809 Hz |  2.52 | -1.8 dB |
| Peaking | 2755 Hz |  4.39 | 1.2 dB  |
| Peaking | 6672 Hz | 12.22 | 1.5 dB  |
| Peaking | 8965 Hz |  4.36 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Listen/Focal%20Listen.png)