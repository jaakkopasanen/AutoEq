# Earsonics Velvet Pot CCW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.1; 28 -0.3; 31 -0.4; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.6; 49 -0.6; 54 -0.6; 60 -0.5; 66 -0.4; 72 -0.3; 79 -0.2; 87 0.1; 96 0.4; 106 1.1; 116 1.7; 128 2.5; 141 3.4; 155 4.5; 170 5.5; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 5.5; 302 4.6; 332 3.9; 365 3.2; 402 2.6; 442 2.2; 486 1.7; 535 1.4; 588 1.5; 647 1.4; 712 1.1; 783 1.1; 861 0.7; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.4; 1526 -1.7; 1678 -1.5; 1846 -0.5; 2031 1.6; 2234 3.3; 2457 4.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CCW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CCW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.63 | -1.8 dB |
| Peaking | 207 Hz  | 0.85 | 7.0 dB  |
| Peaking | 1576 Hz | 1.85 | -4.5 dB |
| Peaking | 3519 Hz | 0.79 | 7.1 dB  |
| Peaking | 2643 Hz | 4.66 | 1.2 dB  |
| Peaking | 3501 Hz | 2.49 | -0.9 dB |
| Peaking | 6120 Hz | 2.57 | 5.3 dB  |
| Peaking | 7276 Hz | 1.4  | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CCW/Earsonics%20Velvet%20Pot%20CCW.png)