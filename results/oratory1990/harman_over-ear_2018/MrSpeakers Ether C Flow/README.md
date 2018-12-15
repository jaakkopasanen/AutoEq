# MrSpeakers Ether C Flow

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.2; 79 5.2; 87 4.3; 96 3.4; 106 3.2; 116 3.2; 128 3.3; 141 3.2; 155 2.8; 170 2.2; 187 1.3; 206 0.6; 227 -0.1; 249 -0.4; 274 -0.5; 302 -0.3; 332 0.2; 365 0.7; 402 1.1; 442 1.5; 486 2.1; 535 1.9; 588 1.6; 647 0.7; 712 -0.8; 783 -1.3; 861 -0.6; 947 -0.1; 1042 0.4; 1146 0.5; 1261 0.0; 1387 0.5; 1526 0.7; 1678 1.6; 1846 2.7; 2031 3.5; 2234 3.7; 2457 4.5; 2703 4.3; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.8; 6373 2.8; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -1.8; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.27 | 4.7 dB  |
| Peaking | 85 Hz   |  0.33 | 3.0 dB  |
| Peaking | 419 Hz  |  0.59 | -4.7 dB |
| Peaking | 483 Hz  |  1.49 | 5.8 dB  |
| Peaking | 3656 Hz |  0.88 | 6.7 dB  |
| Peaking | 771 Hz  | 10.3  | -1.2 dB |
| Peaking | 2043 Hz |  3.69 | 1.2 dB  |
| Peaking | 5393 Hz |  3.17 | 2.8 dB  |
| Peaking | 7702 Hz |  0.38 | -1.1 dB |
| Peaking | 8048 Hz |  6.21 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20C%20Flow/MrSpeakers%20Ether%20C%20Flow.png)