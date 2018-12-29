# Torque t096z Flat Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.8; 28 1.3; 31 1.0; 34 0.7; 37 0.5; 41 0.2; 45 -0.1; 49 -0.4; 54 -0.8; 60 -1.1; 66 -1.6; 72 -2.0; 79 -2.4; 87 -2.9; 96 -3.4; 106 -3.7; 116 -4.0; 128 -4.3; 141 -4.7; 155 -4.9; 170 -5.0; 187 -5.1; 206 -5.2; 227 -5.0; 249 -5.0; 274 -4.8; 302 -4.5; 332 -4.1; 365 -3.6; 402 -3.1; 442 -2.4; 486 -1.9; 535 -1.3; 588 -0.5; 647 0.1; 712 0.3; 783 0.7; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.7; 1526 -4.1; 1678 -5.4; 1846 -6.5; 2031 -6.5; 2234 -5.4; 2457 -2.1; 2703 0.9; 2973 4.2; 3270 5.9; 3597 5.9; 3957 3.5; 4353 -1.1; 4788 -0.2; 5267 5.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Flat Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Flat Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.17 | 2.8 dB  |
| Peaking | 183 Hz  | 0.66 | -5.5 dB |
| Peaking | 1957 Hz | 2.29 | -7.8 dB |
| Peaking | 3276 Hz | 3.38 | 7.7 dB  |
| Peaking | 5946 Hz | 4.23 | 6.7 dB  |
| Peaking | 361 Hz  | 2.11 | -1.1 dB |
| Peaking | 786 Hz  | 1.59 | 1.8 dB  |
| Peaking | 1500 Hz | 4.08 | -1.2 dB |
| Peaking | 4515 Hz | 2.57 | 3.0 dB  |
| Peaking | 4516 Hz | 6.61 | -7.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Flat%20Filter/Torque%20t096z%20Flat%20Filter.png)