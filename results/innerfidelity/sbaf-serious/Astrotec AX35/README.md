# Astrotec AX35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.0; 49 4.3; 54 3.6; 60 2.7; 66 1.8; 72 1.1; 79 0.3; 87 -0.5; 96 -1.3; 106 -2.0; 116 -2.5; 128 -3.0; 141 -3.5; 155 -4.0; 170 -4.2; 187 -4.4; 206 -4.6; 227 -4.6; 249 -4.6; 274 -4.5; 302 -4.3; 332 -4.1; 365 -3.8; 402 -3.5; 442 -3.0; 486 -2.7; 535 -2.2; 588 -1.5; 647 -1.0; 712 -0.7; 783 -0.1; 861 -0.0; 947 0.0; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.9; 1526 -2.8; 1678 -3.0; 1846 -2.6; 2031 -2.0; 2234 -1.3; 2457 0.1; 2703 1.2; 2973 3.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.3; 4788 4.5; 5267 4.5; 5793 2.8; 6373 -0.3; 7010 1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.6  | 6.9 dB  |
| Peaking | 201 Hz  | 0.56 | -5.3 dB |
| Peaking | 1883 Hz | 1.87 | -4.0 dB |
| Peaking | 3768 Hz | 1.49 | 7.0 dB  |
| Peaking | 891 Hz  | 2.5  | 1.2 dB  |
| Peaking | 1490 Hz | 6.69 | -1.0 dB |
| Peaking | 4350 Hz | 3.34 | -0.5 dB |
| Peaking | 5345 Hz | 5.07 | 1.9 dB  |
| Peaking | 6285 Hz | 8.45 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX35/Astrotec%20AX35.png)