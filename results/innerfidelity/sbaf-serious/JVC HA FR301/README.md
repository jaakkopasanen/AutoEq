# JVC HA FR301

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -9.1; 23 -9.6; 25 -10.0; 28 -10.5; 31 -10.9; 34 -11.2; 37 -11.5; 41 -11.9; 45 -12.1; 49 -12.4; 54 -12.7; 60 -13.0; 66 -13.3; 72 -13.6; 79 -13.9; 87 -14.1; 96 -14.4; 106 -14.5; 116 -14.5; 128 -14.5; 141 -14.5; 155 -14.3; 170 -14.1; 187 -13.8; 206 -13.4; 227 -12.8; 249 -12.3; 274 -11.6; 302 -10.9; 332 -10.1; 365 -9.2; 402 -8.3; 442 -7.2; 486 -6.5; 535 -5.4; 588 -4.0; 647 -3.1; 712 -2.3; 783 -1.2; 861 -0.6; 947 -0.1; 1042 0.1; 1146 0.2; 1261 0.0; 1387 -0.6; 1526 -1.3; 1678 -1.8; 1846 -2.2; 2031 -2.5; 2234 -3.0; 2457 -3.5; 2703 -4.8; 2973 -6.0; 3270 -6.7; 3597 -7.1; 3957 -8.0; 4353 -10.7; 4788 -12.4; 5267 -10.5; 5793 -6.9; 6373 -4.2; 7010 -3.3; 7711 -4.4; 8482 -6.6; 9330 -7.0; 10263 -3.7; 11289 0.0; 12418 0.0; 13660 -0.3; 15026 -5.3; 16529 -3.8; 18182 -0.1; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA FR301 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA FR301 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.29 | -11.1 dB |
| Peaking | 160 Hz   | 0.7  | -7.5 dB  |
| Peaking | 336 Hz   | 1.29 | -4.6 dB  |
| Peaking | 4664 Hz  | 1.16 | -11.0 dB |
| Peaking | 15638 Hz | 3.45 | -5.5 dB  |
| Peaking | 1061 Hz  | 2.38 | 2.0 dB   |
| Peaking | 2857 Hz  | 5.36 | -1.1 dB  |
| Peaking | 6789 Hz  | 3.78 | 3.9 dB   |
| Peaking | 9388 Hz  | 2.3  | -7.0 dB  |
| Peaking | 11144 Hz | 2.23 | 4.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA%20FR301/JVC%20HA%20FR301.png)