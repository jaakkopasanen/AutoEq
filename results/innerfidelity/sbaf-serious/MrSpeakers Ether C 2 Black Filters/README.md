# MrSpeakers Ether C 2 Black Filters

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.4; 28 2.4; 31 2.5; 34 2.7; 37 3.0; 41 3.6; 45 4.1; 49 4.1; 54 3.4; 60 2.7; 66 3.2; 72 3.4; 79 3.2; 87 2.9; 96 2.1; 106 1.2; 116 1.8; 128 1.8; 141 2.4; 155 3.3; 170 2.4; 187 1.6; 206 1.1; 227 0.8; 249 0.4; 274 0.3; 302 0.3; 332 0.4; 365 0.6; 402 1.1; 442 1.5; 486 1.5; 535 1.5; 588 1.4; 647 1.2; 712 0.9; 783 0.9; 861 0.3; 947 -0.0; 1042 0.3; 1146 0.9; 1261 0.7; 1387 0.2; 1526 -0.0; 1678 -0.3; 1846 0.2; 2031 0.8; 2234 1.4; 2457 1.7; 2703 2.1; 2973 2.6; 3270 2.2; 3597 2.2; 3957 2.4; 4353 2.2; 4788 3.7; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 2 Black Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 2 Black Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.78 | 2.2 dB  |
| Peaking | 48 Hz   | 0.44 | 3.3 dB  |
| Peaking | 160 Hz  | 5.46 | 2.2 dB  |
| Peaking | 3005 Hz | 1.68 | 2.1 dB  |
| Peaking | 5703 Hz | 2.92 | 6.4 dB  |
| Peaking | 340 Hz  | 1.17 | -1.0 dB |
| Peaking | 480 Hz  | 1.32 | 1.9 dB  |
| Peaking | 1696 Hz | 5.67 | -1.2 dB |
| Peaking | 2994 Hz | 0.35 | 0.1 dB  |
| Peaking | 8291 Hz | 3.99 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%202%20Black%20Filters/MrSpeakers%20Ether%20C%202%20Black%20Filters.png)