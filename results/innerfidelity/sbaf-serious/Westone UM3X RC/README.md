# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.4; 28 2.0; 31 1.7; 34 1.5; 37 1.2; 41 1.0; 45 0.7; 49 0.4; 54 0.2; 60 -0.3; 66 -0.6; 72 -0.9; 79 -1.4; 87 -1.8; 96 -2.3; 106 -2.6; 116 -2.8; 128 -3.1; 141 -3.3; 155 -3.5; 170 -3.6; 187 -3.7; 206 -3.6; 227 -3.5; 249 -3.5; 274 -3.3; 302 -3.1; 332 -2.9; 365 -2.6; 402 -2.3; 442 -1.8; 486 -1.5; 535 -1.1; 588 -0.4; 647 -0.1; 712 0.0; 783 0.4; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.1; 1526 -1.4; 1678 -1.3; 1846 -0.4; 2031 1.3; 2234 3.2; 2457 5.5; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.3  | 3.4 dB  |
| Peaking | 196 Hz   | 0.45 | -4.0 dB |
| Peaking | 1622 Hz  | 1.46 | -6.9 dB |
| Peaking | 3476 Hz  | 0.37 | 8.1 dB  |
| Peaking | 9194 Hz  | 1.27 | -4.6 dB |
| Peaking | 2547 Hz  | 7.77 | 1.5 dB  |
| Peaking | 6233 Hz  | 2.48 | 5.2 dB  |
| Peaking | 7217 Hz  | 1.14 | -5.4 dB |
| Peaking | 9176 Hz  | 1.61 | 3.3 dB  |
| Peaking | 15691 Hz | 1.16 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)