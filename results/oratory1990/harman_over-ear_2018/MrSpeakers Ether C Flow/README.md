# MrSpeakers Ether C Flow

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.6; 28 2.1; 31 2.8; 34 3.7; 37 4.8; 41 4.9; 45 2.9; 49 1.2; 54 2.5; 60 4.5; 66 2.0; 72 0.8; 79 1.0; 87 0.5; 96 0.1; 106 0.3; 116 0.8; 128 1.5; 141 1.8; 155 1.8; 170 1.6; 187 1.0; 206 0.5; 227 -0.1; 249 -0.4; 274 -0.5; 302 -0.3; 332 0.2; 365 0.7; 402 1.1; 442 1.5; 486 2.1; 535 1.9; 588 1.6; 647 0.7; 712 -0.8; 783 -1.3; 861 -0.6; 947 -0.1; 1042 0.4; 1146 0.5; 1261 0.0; 1387 0.5; 1526 0.7; 1678 1.6; 1846 2.7; 2031 3.5; 2234 3.7; 2457 4.5; 2703 4.3; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.8; 6373 2.8; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -1.8; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.24 | 4.2 dB  |
| Peaking | 151 Hz   | 3.5  | 1.8 dB  |
| Peaking | 525 Hz   | 2.51 | 2.4 dB  |
| Peaking | 777 Hz   | 2.86 | -2.0 dB |
| Peaking | 3756 Hz  | 0.95 | 6.7 dB  |
| Peaking | 272 Hz   | 4.45 | -1.0 dB |
| Peaking | 1358 Hz  | 5.74 | -0.8 dB |
| Peaking | 5484 Hz  | 5.95 | 2.2 dB  |
| Peaking | 8525 Hz  | 2.33 | -1.6 dB |
| Peaking | 13582 Hz | 5.81 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20C%20Flow/MrSpeakers%20Ether%20C%20Flow.png)