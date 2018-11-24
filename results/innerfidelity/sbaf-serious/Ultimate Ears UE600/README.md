# Ultimate Ears UE600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 3.1; 28 3.0; 31 2.9; 34 2.8; 37 2.7; 41 2.5; 45 2.3; 49 2.2; 54 2.0; 60 1.7; 66 1.4; 72 1.0; 79 0.6; 87 0.1; 96 -0.4; 106 -0.7; 116 -0.7; 128 -1.1; 141 -1.4; 155 -1.7; 170 -1.9; 187 -1.9; 206 -2.0; 227 -2.0; 249 -2.0; 274 -1.9; 302 -1.8; 332 -1.7; 365 -1.6; 402 -1.4; 442 -1.1; 486 -1.1; 535 -0.9; 588 -0.1; 647 0.1; 712 0.2; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.2; 1387 -0.4; 1526 -0.5; 1678 -0.3; 1846 0.5; 2031 1.5; 2234 2.5; 2457 4.1; 2703 5.1; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.6; 4353 3.4; 4788 3.4; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.62 | 3.2 dB  |
| Peaking | 55 Hz   | 1.37 | 1.1 dB  |
| Peaking | 212 Hz  | 0.64 | -2.2 dB |
| Peaking | 3226 Hz | 1.81 | 6.5 dB  |
| Peaking | 5826 Hz | 3.47 | 5.7 dB  |
| Peaking | 764 Hz  | 3    | 0.8 dB  |
| Peaking | 1575 Hz | 2.44 | -1.2 dB |
| Peaking | 2467 Hz | 5.31 | 1.1 dB  |
| Peaking | 6615 Hz | 9.02 | 1.8 dB  |
| Peaking | 8202 Hz | 2.37 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)