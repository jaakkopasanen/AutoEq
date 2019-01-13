# Philips O'Neil Bend
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.0; 28 1.4; 31 0.9; 34 0.4; 37 -0.1; 41 -0.5; 45 -0.9; 49 -1.3; 54 -1.7; 60 -2.0; 66 -2.4; 72 -2.7; 79 -3.1; 87 -3.6; 96 -3.9; 106 -4.1; 116 -4.2; 128 -4.2; 141 -4.6; 155 -4.8; 170 -4.2; 187 -4.3; 206 -4.1; 227 -3.7; 249 -3.3; 274 -2.6; 302 -2.0; 332 -1.4; 365 -1.0; 402 -0.7; 442 -0.4; 486 -0.3; 535 -0.4; 588 -0.2; 647 -0.2; 712 -0.3; 783 -0.2; 861 -0.4; 947 -0.2; 1042 0.0; 1146 0.6; 1261 1.3; 1387 1.7; 1526 2.4; 1678 3.0; 1846 4.0; 2031 5.1; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.6; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips O'Neil Bend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips O'Neil Bend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.13 | 4.5 dB  |
| Peaking | 100 Hz  | 0.65 | -3.1 dB |
| Peaking | 189 Hz  | 1.02 | -2.7 dB |
| Peaking | 2792 Hz | 1.03 | 6.5 dB  |
| Peaking | 5644 Hz | 2.9  | 4.8 dB  |
| Peaking | 953 Hz  | 2.94 | -1.0 dB |
| Peaking | 2143 Hz | 3.2  | 1.1 dB  |
| Peaking | 2758 Hz | 3.1  | -1.1 dB |
| Peaking | 3843 Hz | 5.33 | 1.2 dB  |
| Peaking | 8438 Hz | 3.46 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20O'Neil%20Bend/Philips%20O'Neil%20Bend.png)