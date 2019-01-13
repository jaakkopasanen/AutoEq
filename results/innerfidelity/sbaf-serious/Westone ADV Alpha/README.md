# Westone ADV Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.3; 28 -7.3; 31 -7.4; 34 -7.5; 37 -7.5; 41 -7.6; 45 -7.6; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.3; 72 -8.5; 79 -8.7; 87 -8.9; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.2; 155 -9.0; 170 -8.9; 187 -8.5; 206 -8.3; 227 -7.7; 249 -7.4; 274 -6.8; 302 -6.2; 332 -5.7; 365 -5.0; 402 -4.4; 442 -3.6; 486 -3.1; 535 -2.4; 588 -1.5; 647 -1.0; 712 -0.6; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.0; 1261 -0.1; 1387 -0.4; 1526 -0.6; 1678 0.1; 1846 0.7; 2031 1.5; 2234 2.3; 2457 3.6; 2703 4.8; 2973 6.0; 3270 6.0; 3597 5.9; 3957 3.2; 4353 -1.5; 4788 -3.9; 5267 -0.7; 5793 3.2; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone ADV Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone ADV Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.2  | -6.9 dB |
| Peaking | 138 Hz   | 0.67 | -5.3 dB |
| Peaking | 287 Hz   | 1.08 | -3.1 dB |
| Peaking | 3061 Hz  | 2.42 | 6.8 dB  |
| Peaking | 21542 Hz | 2.25 | 2.6 dB  |
| Peaking | 842 Hz   | 2.69 | 0.9 dB  |
| Peaking | 1493 Hz  | 5.41 | -0.9 dB |
| Peaking | 3758 Hz  | 6.12 | 3.2 dB  |
| Peaking | 4708 Hz  | 4.13 | -6.2 dB |
| Peaking | 6250 Hz  | 4.61 | 6.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20ADV%20Alpha/Westone%20ADV%20Alpha.png)