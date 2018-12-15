# MrSpeakers Ether Flow

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.4; 66 3.1; 72 2.3; 79 2.2; 87 1.6; 96 0.5; 106 -0.3; 116 -0.9; 128 -1.6; 141 -2.4; 155 -3.0; 170 -3.5; 187 -3.9; 206 -4.1; 227 -4.0; 249 -3.7; 274 -3.1; 302 -2.4; 332 -2.0; 365 -1.0; 402 -0.0; 442 1.2; 486 2.3; 535 1.7; 588 0.8; 647 1.0; 712 0.8; 783 0.0; 861 -0.0; 947 0.2; 1042 0.5; 1146 2.2; 1261 2.1; 1387 1.8; 1526 1.9; 1678 1.2; 1846 1.4; 2031 0.8; 2234 1.3; 2457 0.8; 2703 1.1; 2973 1.5; 3270 3.1; 3597 5.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.4; 5793 0.0; 6373 -2.8; 7010 -3.1; 7711 -2.0; 8482 0.0; 9330 0.0; 10263 -2.1; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.45 | 7.1 dB  |
| Peaking | 243 Hz   | 0.54 | -8.5 dB |
| Peaking | 419 Hz   | 0.66 | 6.1 dB  |
| Peaking | 4678 Hz  | 1.5  | 8.8 dB  |
| Peaking | 6481 Hz  | 2.08 | -7.1 dB |
| Peaking | 486 Hz   | 7.79 | 1.6 dB  |
| Peaking | 990 Hz   | 1.59 | -3.3 dB |
| Peaking | 1172 Hz  | 1.8  | 3.9 dB  |
| Peaking | 2705 Hz  | 4.8  | -1.1 dB |
| Peaking | 24000 Hz | 1.84 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)