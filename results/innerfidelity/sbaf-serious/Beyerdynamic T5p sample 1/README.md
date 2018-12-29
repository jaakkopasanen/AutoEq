# Beyerdynamic T5p sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -0.9; 25 -0.8; 28 -0.5; 31 -0.2; 34 0.1; 37 0.4; 41 0.7; 45 1.0; 49 1.1; 54 1.4; 60 2.0; 66 2.8; 72 3.2; 79 2.3; 87 0.3; 96 -1.7; 106 -2.4; 116 -2.5; 128 -2.2; 141 -1.6; 155 -0.6; 170 -0.3; 187 -0.7; 206 -0.2; 227 0.4; 249 0.9; 274 1.4; 302 1.7; 332 2.0; 365 2.2; 402 2.3; 442 2.5; 486 2.3; 535 2.6; 588 3.5; 647 5.6; 712 2.7; 783 2.0; 861 1.5; 947 1.3; 1042 -0.1; 1146 0.4; 1261 -0.1; 1387 -2.3; 1526 -0.8; 1678 -0.9; 1846 -0.2; 2031 -0.7; 2234 -2.1; 2457 -0.6; 2703 0.9; 2973 1.7; 3270 3.1; 3597 4.0; 3957 4.2; 4353 3.1; 4788 6.0; 5267 5.7; 5793 1.0; 6373 0.1; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 1.85 | 5.3 dB  |
| Peaking | 103 Hz  | 1.47 | -4.5 dB |
| Peaking | 373 Hz  | 1.45 | 2.4 dB  |
| Peaking | 653 Hz  | 4.33 | 4.8 dB  |
| Peaking | 4605 Hz | 2.23 | 5.6 dB  |
| Peaking | 21 Hz   | 1.77 | -1.1 dB |
| Peaking | 1401 Hz | 6.81 | -2.4 dB |
| Peaking | 2255 Hz | 6.44 | -2.8 dB |
| Peaking | 3395 Hz | 4.46 | 2.2 dB  |
| Peaking | 6069 Hz | 0.56 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sample%201/Beyerdynamic%20T5p%20sample%201.png)