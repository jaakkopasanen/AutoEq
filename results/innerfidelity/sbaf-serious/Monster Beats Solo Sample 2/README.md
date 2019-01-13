# Monster Beats Solo sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.0; 31 4.4; 34 3.9; 37 3.2; 41 2.4; 45 2.4; 49 2.7; 54 2.7; 60 2.0; 66 1.3; 72 0.4; 79 -1.3; 87 -2.8; 96 -3.9; 106 -4.9; 116 -5.6; 128 -5.9; 141 -6.1; 155 -6.2; 170 -6.2; 187 -6.0; 206 -4.9; 227 -4.7; 249 -5.5; 274 -5.2; 302 -3.2; 332 -0.8; 365 1.4; 402 2.1; 442 3.1; 486 3.6; 535 2.9; 588 2.3; 647 1.4; 712 0.5; 783 0.2; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.9; 1387 0.9; 1526 1.3; 1678 2.0; 1846 3.1; 2031 4.3; 2234 5.1; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.5; 4353 2.9; 4788 4.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.27 | 6.8 dB  |
| Peaking | 134 Hz  | 1.26 | -7.5 dB |
| Peaking | 254 Hz  | 4.55 | -4.4 dB |
| Peaking | 2881 Hz | 1.12 | 6.3 dB  |
| Peaking | 5762 Hz | 3.42 | 5.1 dB  |
| Peaking | 92 Hz   | 2.52 | -3.8 dB |
| Peaking | 95 Hz   | 0.84 | 5.0 dB  |
| Peaking | 205 Hz  | 0.25 | -3.0 dB |
| Peaking | 464 Hz  | 1.54 | 6.2 dB  |
| Peaking | 8405 Hz | 4.03 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%202/Monster%20Beats%20Solo%20sample%202.png)