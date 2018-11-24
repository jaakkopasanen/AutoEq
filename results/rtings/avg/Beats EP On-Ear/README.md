# Beats EP On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 -1.2; 23 -1.3; 25 -1.4; 28 -1.6; 31 -1.7; 34 -1.8; 37 -1.8; 41 -1.8; 45 -1.8; 49 -1.9; 54 -2.1; 60 -2.5; 66 -2.9; 72 -3.1; 79 -3.4; 87 -3.7; 96 -4.0; 106 -4.3; 116 -4.6; 128 -4.8; 141 -5.0; 155 -5.2; 170 -5.1; 187 -5.0; 206 -4.9; 227 -4.7; 249 -4.1; 274 -3.6; 302 -2.9; 332 -2.6; 365 -2.3; 402 -2.2; 442 -2.0; 486 -1.7; 535 -1.2; 588 -0.8; 647 -0.4; 712 -0.1; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -0.8; 1526 -1.2; 1678 -1.5; 1846 -1.9; 2031 -2.1; 2234 -1.3; 2457 -0.0; 2703 0.7; 2973 0.2; 3270 -0.1; 3597 0.3; 3957 0.6; 4353 -0.5; 4788 -2.8; 5267 -0.2; 5793 2.7; 6373 1.5; 7010 -0.8; 7711 -1.4; 8482 -1.9; 9330 -2.3; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 -1.1; 15026 -1.9; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats EP On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats EP On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 0.31 | -1.5 dB |
| Peaking | 172 Hz   | 0.69 | -4.4 dB |
| Peaking | 1893 Hz  | 4.06 | -2.1 dB |
| Peaking | 6039 Hz  | 5.84 | 4.7 dB  |
| Peaking | 7588 Hz  | 1.05 | -2.1 dB |
| Peaking | 811 Hz   | 3.55 | 0.9 dB  |
| Peaking | 4300 Hz  | 1.93 | 1.6 dB  |
| Peaking | 4803 Hz  | 6.69 | -4.0 dB |
| Peaking | 11746 Hz | 4.38 | 1.1 dB  |
| Peaking | 14810 Hz | 3.76 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20EP%20On-Ear/Beats%20EP%20On-Ear.png)