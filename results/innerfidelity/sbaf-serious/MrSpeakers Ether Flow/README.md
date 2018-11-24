# MrSpeakers Ether Flow

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.9; 28 2.4; 31 2.9; 34 3.2; 37 3.1; 41 2.5; 45 1.5; 49 0.8; 54 1.0; 60 0.4; 66 -0.3; 72 -0.9; 79 -1.1; 87 -2.0; 96 -2.6; 106 -2.8; 116 -2.9; 128 -3.1; 141 -3.2; 155 -2.9; 170 -3.2; 187 -3.3; 206 -3.2; 227 -2.9; 249 -2.7; 274 -2.1; 302 -1.5; 332 -1.0; 365 -0.5; 402 0.2; 442 0.7; 486 1.0; 535 1.2; 588 1.7; 647 2.0; 712 1.5; 783 1.5; 861 1.1; 947 1.0; 1042 0.1; 1146 2.3; 1261 2.6; 1387 2.1; 1526 0.8; 1678 -0.0; 1846 -0.5; 2031 -0.3; 2234 0.3; 2457 1.0; 2703 1.8; 2973 1.0; 3270 0.5; 3597 0.3; 3957 0.4; 4353 -0.1; 4788 0.1; 5267 1.1; 5793 1.1; 6373 -1.4; 7010 -0.6; 7711 0.3; 8482 -0.4; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.83 | 3.7 dB  |
| Peaking | 155 Hz  | 0.45 | -3.8 dB |
| Peaking | 560 Hz  | 1.12 | 2.9 dB  |
| Peaking | 1257 Hz | 5.41 | 2.7 dB  |
| Peaking | 2708 Hz | 5.4  | 1.8 dB  |
| Peaking | 374 Hz  | 3.86 | 0.2 dB  |
| Peaking | 1898 Hz | 6.13 | -1.0 dB |
| Peaking | 5670 Hz | 4.91 | 1.9 dB  |
| Peaking | 6374 Hz | 6.22 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)