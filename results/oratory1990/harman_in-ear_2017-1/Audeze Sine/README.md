# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.9; 28 5.7; 31 5.6; 34 5.6; 37 5.6; 41 5.4; 45 5.2; 49 5.0; 54 4.7; 60 4.3; 66 3.8; 72 3.5; 79 3.3; 87 3.0; 96 2.3; 106 1.9; 116 1.6; 128 1.2; 141 1.0; 155 0.7; 170 0.7; 187 0.9; 206 1.1; 227 0.7; 249 0.4; 274 0.2; 302 0.2; 332 0.2; 365 0.4; 402 0.4; 442 0.1; 486 -0.0; 535 0.1; 588 0.2; 647 0.4; 712 0.5; 783 0.5; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.4; 1261 -0.5; 1387 -0.6; 1526 -0.2; 1678 -0.0; 1846 -0.4; 2031 -0.5; 2234 -0.1; 2457 0.8; 2703 0.5; 2973 0.3; 3270 0.1; 3597 0.0; 3957 1.7; 4353 3.9; 4788 4.7; 5267 4.9; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -3.6; 11289 -5.8; 12418 -6.3; 13660 -11.5; 15026 -19.0; 16529 -23.9; 18182 -23.4; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.67 | 4.5 dB   |
| Peaking | 46 Hz    | 0.63 | 3.8 dB   |
| Peaking | 85 Hz    | 3.24 | 0.4 dB   |
| Peaking | 7155 Hz  | 0.74 | 10.2 dB  |
| Peaking | 17475 Hz | 0.61 | -26.9 dB |
| Peaking | 3740 Hz  | 1    | -4.0 dB  |
| Peaking | 5040 Hz  | 1.02 | 4.8 dB   |
| Peaking | 7540 Hz  | 4.36 | -4.4 dB  |
| Peaking | 12680 Hz | 4.53 | 3.4 dB   |
| Peaking | 15361 Hz | 4.28 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine/Audeze%20Sine.png)