# Audeze SINE DX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.8; 45 5.8; 49 5.8; 54 5.6; 60 5.4; 66 5.2; 72 5.0; 79 4.8; 87 4.5; 96 4.2; 106 4.0; 116 3.8; 128 3.6; 141 3.3; 155 3.1; 170 3.0; 187 3.1; 206 3.0; 227 3.0; 249 2.9; 274 2.8; 302 2.7; 332 2.7; 365 2.6; 402 2.5; 442 2.5; 486 2.2; 535 2.1; 588 2.5; 647 2.6; 712 2.0; 783 1.7; 861 1.0; 947 0.4; 1042 -0.4; 1146 -1.1; 1261 -1.8; 1387 -2.1; 1526 -3.7; 1678 -3.2; 1846 -1.5; 2031 0.9; 2234 3.0; 2457 4.6; 2703 5.0; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze SINE DX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE DX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.27 | 4.9 dB  |
| Peaking | 126 Hz  | 0.19 | 2.6 dB  |
| Peaking | 635 Hz  | 2.36 | 1.1 dB  |
| Peaking | 1563 Hz | 1.91 | -6.3 dB |
| Peaking | 3601 Hz | 0.79 | 7.2 dB  |
| Peaking | 1075 Hz | 6.38 | -0.6 dB |
| Peaking | 2412 Hz | 5.74 | 1.1 dB  |
| Peaking | 3744 Hz | 3.78 | -0.9 dB |
| Peaking | 6254 Hz | 2.34 | 5.5 dB  |
| Peaking | 7332 Hz | 1.42 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE%20DX/Audeze%20SINE%20DX.png)