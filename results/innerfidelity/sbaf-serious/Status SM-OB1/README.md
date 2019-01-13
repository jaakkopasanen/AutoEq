# Status SM-OB1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.8; 41 4.0; 45 3.4; 49 2.9; 54 2.3; 60 1.8; 66 1.3; 72 1.0; 79 0.9; 87 0.6; 96 0.0; 106 -0.3; 116 -0.8; 128 -1.3; 141 -1.5; 155 -1.5; 170 -1.4; 187 -1.5; 206 -1.4; 227 -1.0; 249 -0.5; 274 -0.6; 302 -1.2; 332 -0.9; 365 -0.5; 402 -0.4; 442 -0.3; 486 -0.5; 535 -0.4; 588 -0.3; 647 -0.3; 712 -0.2; 783 -0.1; 861 -0.2; 947 -0.1; 1042 0.3; 1146 1.1; 1261 1.2; 1387 1.3; 1526 1.6; 1678 2.5; 1846 3.3; 2031 3.6; 2234 3.5; 2457 3.8; 2703 4.4; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Status SM-OB1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-OB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.73 | 6.3 dB  |
| Peaking | 150 Hz  | 1.23 | -1.9 dB |
| Peaking | 372 Hz  | 0.98 | -0.6 dB |
| Peaking | 880 Hz  | 3.82 | -0.6 dB |
| Peaking | 3822 Hz | 0.81 | 6.6 dB  |
| Peaking | 1861 Hz | 5.55 | 1.1 dB  |
| Peaking | 3886 Hz | 4.26 | -0.6 dB |
| Peaking | 6246 Hz | 2.45 | 5.3 dB  |
| Peaking | 7371 Hz | 1.46 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-OB1/Status%20SM-OB1.png)