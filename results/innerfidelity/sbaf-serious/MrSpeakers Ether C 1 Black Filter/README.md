# MrSpeakers Ether C 1 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.5; 28 2.5; 31 2.6; 34 2.9; 37 3.1; 41 3.6; 45 4.3; 49 4.4; 54 3.4; 60 2.7; 66 2.8; 72 3.9; 79 3.6; 87 2.6; 96 2.4; 106 1.9; 116 2.3; 128 2.2; 141 3.0; 155 3.8; 170 3.0; 187 2.0; 206 1.5; 227 1.2; 249 0.9; 274 0.7; 302 0.6; 332 0.6; 365 1.0; 402 1.5; 442 2.2; 486 2.3; 535 1.8; 588 1.5; 647 1.2; 712 0.9; 783 0.8; 861 0.1; 947 -0.1; 1042 0.3; 1146 1.0; 1261 1.0; 1387 0.9; 1526 0.7; 1678 0.1; 1846 0.7; 2031 1.3; 2234 1.3; 2457 1.4; 2703 1.4; 2973 1.7; 3270 1.6; 3597 1.9; 3957 2.4; 4353 2.0; 4788 3.0; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 1 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.4  | 2.3 dB  |
| Peaking | 52 Hz   | 0.61 | 3.6 dB  |
| Peaking | 157 Hz  | 3.75 | 2.8 dB  |
| Peaking | 499 Hz  | 1.71 | 2.0 dB  |
| Peaking | 5634 Hz | 2.3  | 6.2 dB  |
| Peaking | 3100 Hz | 0.86 | 1.3 dB  |
| Peaking | 4570 Hz | 6.49 | -1.4 dB |
| Peaking | 6520 Hz | 5.91 | 2.3 dB  |
| Peaking | 7382 Hz | 1.26 | -1.3 dB |
| Peaking | 7523 Hz | 4.35 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%201%20Black%20Filter/MrSpeakers%20Ether%20C%201%20Black%20Filter.png)