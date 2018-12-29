# BlueAnt Embrace
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.6; 54 4.5; 60 3.7; 66 3.0; 72 2.2; 79 1.5; 87 0.6; 96 -0.2; 106 -0.8; 116 -1.2; 128 -1.9; 141 -2.4; 155 -2.7; 170 -2.6; 187 -2.8; 206 -2.7; 227 -1.9; 249 -1.3; 274 -1.2; 302 -1.0; 332 -0.2; 365 0.8; 402 2.2; 442 3.5; 486 4.5; 535 5.1; 588 5.9; 647 5.8; 712 5.0; 783 3.3; 861 1.6; 947 0.5; 1042 -0.3; 1146 -0.6; 1261 -0.7; 1387 -0.9; 1526 -1.3; 1678 -1.3; 1846 -0.7; 2031 0.3; 2234 2.5; 2457 3.4; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 3.4; 5267 -0.4; 5793 0.8; 6373 2.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BlueAnt Embrace GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BlueAnt Embrace ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.41 | 6.9 dB  |
| Peaking | 144 Hz   |  0.64 | -4.6 dB |
| Peaking | 569 Hz   |  1.92 | 6.9 dB  |
| Peaking | 3505 Hz  |  1.8  | 7.0 dB  |
| Peaking | 24000 Hz |  2.27 | 0.6 dB  |
| Peaking | 726 Hz   |  5.56 | 2.0 dB  |
| Peaking | 1569 Hz  |  1.23 | -2.4 dB |
| Peaking | 2633 Hz  |  3.55 | 2.6 dB  |
| Peaking | 5424 Hz  | 10.38 | -2.9 dB |
| Peaking | 6726 Hz  |  9.32 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BlueAnt%20Embrace/BlueAnt%20Embrace.png)