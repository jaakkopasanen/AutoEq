# Shure SRH440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.3; 31 4.7; 34 4.2; 37 3.8; 41 3.4; 45 3.0; 49 2.7; 54 2.4; 60 2.0; 66 1.5; 72 0.9; 79 0.0; 87 -0.9; 96 -1.4; 106 -1.6; 116 -1.2; 128 -0.5; 141 -0.2; 155 0.2; 170 0.9; 187 1.4; 206 1.6; 227 1.3; 249 0.9; 274 0.3; 302 -0.3; 332 -1.0; 365 -1.7; 402 -1.7; 442 -1.5; 486 -1.4; 535 -1.1; 588 -1.0; 647 -0.8; 712 -0.5; 783 -0.3; 861 -0.1; 947 -0.1; 1042 0.1; 1146 -0.8; 1261 -1.4; 1387 -1.7; 1526 -1.9; 1678 -2.4; 1846 -3.0; 2031 -2.8; 2234 -1.6; 2457 0.1; 2703 0.3; 2973 0.2; 3270 -0.8; 3597 -1.1; 3957 -0.9; 4353 -0.7; 4788 -0.4; 5267 -0.5; 5793 0.2; 6373 0.3; 7010 -0.7; 7711 -1.9; 8482 -3.0; 9330 -4.7; 10263 -4.3; 11289 -1.2; 12418 -0.1; 13660 -1.7; 15026 -1.8; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.41 | 6.1 dB  |
| Peaking | 44 Hz    | 2.26 | 2.0 dB  |
| Peaking | 432 Hz   | 2.52 | -1.9 dB |
| Peaking | 1788 Hz  | 2.4  | -3.0 dB |
| Peaking | 9570 Hz  | 2.94 | -5.1 dB |
| Peaking | 103 Hz   | 3.05 | -2.2 dB |
| Peaking | 205 Hz   | 2.91 | 1.9 dB  |
| Peaking | 2738 Hz  | 4.76 | 1.4 dB  |
| Peaking | 3541 Hz  | 3.82 | -1.0 dB |
| Peaking | 14607 Hz | 5.07 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH440/Shure%20SRH440.png)