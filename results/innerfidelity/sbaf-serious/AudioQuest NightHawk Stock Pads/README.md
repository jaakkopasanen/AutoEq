# AudioQuest NightHawk Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -6.7; 23 -6.7; 25 -6.7; 28 -6.6; 31 -6.6; 34 -6.5; 37 -6.5; 41 -6.5; 45 -6.4; 49 -6.4; 54 -6.4; 60 -6.4; 66 -6.5; 72 -6.6; 79 -6.9; 87 -7.5; 96 -8.4; 106 -9.1; 116 -8.8; 128 -9.4; 141 -10.0; 155 -9.9; 170 -9.5; 187 -10.1; 206 -10.0; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.4; 332 -9.1; 365 -8.7; 402 -8.1; 442 -7.3; 486 -6.8; 535 -6.0; 588 -4.9; 647 -3.9; 712 -3.0; 783 -2.1; 861 -1.3; 947 -0.4; 1042 -0.2; 1146 -0.8; 1261 -1.2; 1387 -2.8; 1526 -4.1; 1678 -4.5; 1846 -4.0; 2031 -3.1; 2234 -2.1; 2457 -0.1; 2703 2.1; 2973 2.4; 3270 0.3; 3597 -0.1; 3957 2.2; 4353 1.9; 4788 2.4; 5267 2.1; 5793 -0.4; 6373 -0.8; 7010 -2.0; 7711 -3.5; 8482 -4.9; 9330 -5.1; 10263 -2.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -1.1; 18182 -3.8; 20000 -6.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightHawk Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.08 | -5.7 dB |
| Peaking | 359 Hz  | 0.39 | -8.3 dB |
| Peaking | 1414 Hz | 0.4  | 7.6 dB  |
| Peaking | 1725 Hz | 1.44 | -9.8 dB |
| Peaking | 8625 Hz | 2.48 | -6.1 dB |
| Peaking | 54 Hz   | 0.43 | -1.1 dB |
| Peaking | 64 Hz   | 1.43 | 1.9 dB  |
| Peaking | 989 Hz  | 0.11 | 0.3 dB  |
| Peaking | 4789 Hz | 1.39 | -2.8 dB |
| Peaking | 4812 Hz | 3.11 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightHawk%20Stock%20Pads/AudioQuest%20NightHawk%20Stock%20Pads.png)