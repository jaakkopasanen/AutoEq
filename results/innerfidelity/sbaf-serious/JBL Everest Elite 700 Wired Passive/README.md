# JBL Everest Elite 700 Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.8; 28 3.8; 31 3.9; 34 4.0; 37 4.1; 41 4.2; 45 4.3; 49 4.5; 54 4.7; 60 4.7; 66 4.9; 72 5.3; 79 5.6; 87 5.4; 96 4.5; 106 4.2; 116 4.1; 128 4.0; 141 3.8; 155 3.9; 170 3.5; 187 2.8; 206 2.3; 227 2.1; 249 1.8; 274 1.7; 302 1.8; 332 1.9; 365 2.4; 402 1.7; 442 0.0; 486 -0.2; 535 -0.1; 588 0.4; 647 0.3; 712 0.1; 783 0.3; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.7; 1387 -0.4; 1526 -0.6; 1678 -0.9; 1846 -1.1; 2031 -0.8; 2234 -0.3; 2457 0.7; 2703 1.9; 2973 2.9; 3270 4.7; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.6  | 3.1 dB  |
| Peaking | 75 Hz   | 0.8  | 3.8 dB  |
| Peaking | 174 Hz  | 0.65 | 1.8 dB  |
| Peaking | 1919 Hz | 1.5  | -2.4 dB |
| Peaking | 4363 Hz | 1.17 | 7.1 dB  |
| Peaking | 384 Hz  | 4.78 | 2.8 dB  |
| Peaking | 430 Hz  | 2.67 | -1.8 dB |
| Peaking | 4553 Hz | 6.34 | -1.2 dB |
| Peaking | 6397 Hz | 2.73 | 4.3 dB  |
| Peaking | 7500 Hz | 1.86 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wired%20Passive/JBL%20Everest%20Elite%20700%20Wired%20Passive.png)