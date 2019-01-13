# Ultimate Ears UE600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.1; 25 2.0; 28 1.9; 31 1.9; 34 1.8; 37 1.7; 41 1.5; 45 1.3; 49 1.2; 54 0.9; 60 0.7; 66 0.4; 72 0.1; 79 -0.2; 87 -0.6; 96 -0.9; 106 -1.1; 116 -1.3; 128 -1.6; 141 -1.9; 155 -2.2; 170 -2.4; 187 -2.5; 206 -2.6; 227 -2.6; 249 -2.5; 274 -2.4; 302 -2.3; 332 -2.0; 365 -1.8; 402 -1.5; 442 -1.3; 486 -1.1; 535 -0.8; 588 -0.6; 647 -0.2; 712 0.2; 783 0.4; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.0; 1678 -0.9; 1846 -0.2; 2031 0.6; 2234 1.9; 2457 3.4; 2703 4.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 4.3; 4788 4.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.49 | 2.2 dB  |
| Peaking | 206 Hz   | 0.64 | -2.8 dB |
| Peaking | 3237 Hz  | 2.1  | 5.9 dB  |
| Peaking | 5950 Hz  | 1.84 | 6.7 dB  |
| Peaking | 7757 Hz  | 1.96 | -2.8 dB |
| Peaking | 807 Hz   | 2.74 | 1.0 dB  |
| Peaking | 1629 Hz  | 2.08 | -1.7 dB |
| Peaking | 2349 Hz  | 4.32 | 0.5 dB  |
| Peaking | 2648 Hz  | 6.42 | 1.0 dB  |
| Peaking | 12679 Hz | 2.27 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)