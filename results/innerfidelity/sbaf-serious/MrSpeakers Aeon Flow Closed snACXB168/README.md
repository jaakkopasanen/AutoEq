# MrSpeakers Aeon Flow Closed snACXB168

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.4; 28 0.4; 31 0.4; 34 0.3; 37 0.2; 41 0.2; 45 0.1; 49 0.0; 54 0.2; 60 0.6; 66 0.8; 72 0.6; 79 -0.0; 87 -0.5; 96 -0.6; 106 -0.2; 116 0.2; 128 0.2; 141 0.3; 155 0.9; 170 0.0; 187 -0.3; 206 -0.4; 227 -0.5; 249 -0.7; 274 -0.8; 302 -0.9; 332 -1.0; 365 -0.9; 402 -0.8; 442 -0.7; 486 -1.1; 535 -1.4; 588 -1.4; 647 -1.7; 712 -1.8; 783 -1.5; 861 -1.2; 947 -0.6; 1042 0.4; 1146 -0.6; 1261 -1.0; 1387 -1.4; 1526 -1.5; 1678 -1.4; 1846 -0.9; 2031 0.4; 2234 1.5; 2457 2.2; 2703 1.2; 2973 3.3; 3270 2.2; 3597 1.4; 3957 1.8; 4353 -0.0; 4788 1.7; 5267 3.1; 5793 1.7; 6373 0.7; 7010 -2.0; 7711 -3.5; 8482 -3.9; 9330 -2.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed snACXB168 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed snACXB168 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 596 Hz  | 0.97 | -1.5 dB |
| Peaking | 1625 Hz | 2.88 | -2.0 dB |
| Peaking | 2825 Hz | 1.56 | 2.7 dB  |
| Peaking | 5368 Hz | 4.51 | 3.0 dB  |
| Peaking | 8123 Hz | 3.38 | -4.6 dB |
| Peaking | 24 Hz   | 0.54 | 0.7 dB  |
| Peaking | 67 Hz   | 3.17 | 1.6 dB  |
| Peaking | 118 Hz  | 0.51 | -1.6 dB |
| Peaking | 144 Hz  | 1.63 | 2.1 dB  |
| Peaking | 440 Hz  | 3.14 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168.png)