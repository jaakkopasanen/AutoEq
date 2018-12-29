# Ultimate Ears UE700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.7; 28 2.6; 31 2.5; 34 2.4; 37 2.3; 41 2.2; 45 2.1; 49 1.9; 54 1.7; 60 1.4; 66 1.0; 72 0.7; 79 0.3; 87 -0.1; 96 -0.6; 106 -0.7; 116 -0.9; 128 -1.2; 141 -1.6; 155 -1.8; 170 -1.9; 187 -2.0; 206 -2.0; 227 -2.0; 249 -2.0; 274 -1.9; 302 -1.8; 332 -1.7; 365 -1.5; 402 -1.3; 442 -1.0; 486 -0.9; 535 -0.6; 588 -0.0; 647 0.2; 712 0.3; 783 0.5; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.9; 1526 -1.2; 1678 -1.3; 1846 -0.9; 2031 -0.2; 2234 0.7; 2457 2.4; 2703 4.5; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.3; 5267 6.0; 5793 5.9; 6373 4.9; 7010 2.4; 7711 -0.4; 8482 -3.5; 9330 -4.3; 10263 -1.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.55 | 2.7 dB  |
| Peaking | 52 Hz   | 1.08 | 1.1 dB  |
| Peaking | 204 Hz  | 0.57 | -2.2 dB |
| Peaking | 4586 Hz | 0.98 | 7.0 dB  |
| Peaking | 8944 Hz | 3.27 | -6.8 dB |
| Peaking | 778 Hz  | 1.7  | 1.1 dB  |
| Peaking | 1853 Hz | 1.2  | -2.7 dB |
| Peaking | 2909 Hz | 2.87 | 3.6 dB  |
| Peaking | 4666 Hz | 4.14 | -1.6 dB |
| Peaking | 6030 Hz | 4.85 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)