# ZMF Atticus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.2; 28 0.7; 31 0.4; 34 -0.0; 37 -0.4; 41 -0.8; 45 -1.3; 49 -1.7; 54 -2.0; 60 -2.2; 66 -2.8; 72 -3.6; 79 -4.4; 87 -5.2; 96 -6.0; 106 -6.4; 116 -6.7; 128 -7.1; 141 -7.1; 155 -6.5; 170 -6.2; 187 -6.1; 206 -5.4; 227 -4.5; 249 -3.8; 274 -3.2; 302 -2.9; 332 -2.7; 365 -2.6; 402 -2.4; 442 -2.0; 486 -2.3; 535 -2.0; 588 -1.8; 647 -1.7; 712 -1.7; 783 -1.1; 861 -0.9; 947 -0.3; 1042 0.2; 1146 0.4; 1261 0.7; 1387 0.9; 1526 3.2; 1678 2.3; 1846 0.2; 2031 0.5; 2234 -0.6; 2457 -0.3; 2703 0.3; 2973 1.1; 3270 1.2; 3597 3.0; 3957 4.9; 4353 5.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.0; 7711 -1.4; 8482 -2.5; 9330 -2.5; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ZMF Atticus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Atticus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 61 Hz   | 0.23 | 3.8 dB   |
| Peaking | 123 Hz  | 0.48 | -10.1 dB |
| Peaking | 1577 Hz | 8.4  | 4.0 dB   |
| Peaking | 5425 Hz | 1.43 | 7.5 dB   |
| Peaking | 8437 Hz | 2.63 | -5.3 dB  |
| Peaking | 39 Hz   | 2.79 | -0.5 dB  |
| Peaking | 281 Hz  | 3.92 | 0.8 dB   |
| Peaking | 620 Hz  | 2.6  | -0.8 dB  |
| Peaking | 2446 Hz | 3.34 | -1.4 dB  |
| Peaking | 3891 Hz | 8.82 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Atticus/ZMF%20Atticus.png)