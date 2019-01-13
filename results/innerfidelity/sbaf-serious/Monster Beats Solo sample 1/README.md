# Monster Beats Solo sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.8; 23 -5.1; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.8; 41 -5.9; 45 -6.0; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.7; 72 -6.8; 79 -6.8; 87 -6.7; 96 -7.6; 106 -8.4; 116 -8.3; 128 -7.8; 141 -8.2; 155 -9.1; 170 -8.7; 187 -9.1; 206 -8.6; 227 -7.7; 249 -6.6; 274 -5.3; 302 -3.5; 332 -1.8; 365 -0.3; 402 1.3; 442 2.9; 486 3.8; 535 4.1; 588 3.5; 647 2.1; 712 0.9; 783 0.4; 861 -0.1; 947 -0.1; 1042 0.3; 1146 1.0; 1261 1.7; 1387 1.9; 1526 2.0; 1678 2.2; 1846 2.3; 2031 2.9; 2234 2.9; 2457 3.4; 2703 3.8; 2973 4.4; 3270 4.2; 3597 4.5; 3957 3.8; 4353 2.3; 4788 2.0; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.37 | -5.7 dB |
| Peaking | 130 Hz  | 0.92 | -6.2 dB |
| Peaking | 218 Hz  | 1.65 | -6.9 dB |
| Peaking | 996 Hz  | 0.1  | 3.0 dB  |
| Peaking | 521 Hz  | 2.81 | 3.7 dB  |
| Peaking | 885 Hz  | 1.51 | -3.0 dB |
| Peaking | 3456 Hz | 1.46 | 4.5 dB  |
| Peaking | 5622 Hz | 0.75 | -5.7 dB |
| Peaking | 5913 Hz | 2.63 | 8.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%201/Monster%20Beats%20Solo%20sample%201.png)