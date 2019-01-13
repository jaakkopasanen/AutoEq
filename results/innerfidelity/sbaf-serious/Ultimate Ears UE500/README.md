# Ultimate Ears UE500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.7; 23 -8.6; 25 -8.6; 28 -8.5; 31 -8.3; 34 -8.2; 37 -8.1; 41 -7.9; 45 -7.7; 49 -7.6; 54 -7.5; 60 -7.4; 66 -7.3; 72 -7.2; 79 -7.2; 87 -7.2; 96 -7.1; 106 -6.9; 116 -6.7; 128 -6.6; 141 -6.4; 155 -6.1; 170 -5.8; 187 -5.4; 206 -5.1; 227 -4.6; 249 -4.2; 274 -3.8; 302 -3.3; 332 -2.8; 365 -2.3; 402 -1.8; 442 -1.3; 486 -0.9; 535 -0.5; 588 0.1; 647 0.4; 712 0.5; 783 0.8; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.2; 1387 -1.3; 1526 -1.4; 1678 -2.2; 1846 -2.7; 2031 -3.2; 2234 -3.5; 2457 -2.9; 2703 -1.0; 2973 2.4; 3270 5.6; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.2; 7010 0.9; 7711 -0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.45 | -7.6 dB |
| Peaking | 119 Hz  | 0.4  | -5.7 dB |
| Peaking | 693 Hz  | 1.42 | 1.8 dB  |
| Peaking | 2272 Hz | 1.45 | -6.8 dB |
| Peaking | 3914 Hz | 1.11 | 8.7 dB  |
| Peaking | 1257 Hz | 6.93 | -0.6 dB |
| Peaking | 3297 Hz | 7.74 | 1.8 dB  |
| Peaking | 4145 Hz | 3.16 | -1.3 dB |
| Peaking | 6323 Hz | 2.78 | 5.7 dB  |
| Peaking | 7006 Hz | 1.92 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)