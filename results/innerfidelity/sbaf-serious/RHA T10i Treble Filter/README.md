# RHA T10i Treble Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.7; 23 -9.7; 25 -9.8; 28 -10.2; 31 -10.5; 34 -10.6; 37 -10.7; 41 -10.8; 45 -10.9; 49 -11.0; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.3; 87 -11.4; 96 -11.5; 106 -11.3; 116 -11.1; 128 -11.0; 141 -10.8; 155 -10.5; 170 -10.1; 187 -9.7; 206 -9.2; 227 -8.6; 249 -8.1; 274 -7.4; 302 -6.7; 332 -6.1; 365 -5.4; 402 -4.7; 442 -3.9; 486 -3.4; 535 -2.8; 588 -1.9; 647 -1.3; 712 -1.2; 783 -0.5; 861 -0.1; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.6; 1526 -2.5; 1678 -3.4; 1846 -4.2; 2031 -5.1; 2234 -6.4; 2457 -7.0; 2703 -6.1; 2973 -3.9; 3270 -2.1; 3597 -1.7; 3957 -0.1; 4353 2.2; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.6; 8482 -11.1; 9330 -13.4; 10263 -9.9; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Treble Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.24 | -10.4 dB |
| Peaking | 187 Hz   | 0.64 | -4.9 dB  |
| Peaking | 2471 Hz  | 1.69 | -7.8 dB  |
| Peaking | 5870 Hz  | 1.48 | 9.5 dB   |
| Peaking | 9107 Hz  | 3.22 | -17.8 dB |
| Peaking | 919 Hz   | 1.24 | 3.4 dB   |
| Peaking | 946 Hz   | 0.64 | -1.9 dB  |
| Peaking | 10305 Hz | 6.96 | -4.4 dB  |
| Peaking | 11513 Hz | 4.55 | 3.0 dB   |
| Peaking | 13123 Hz | 1.6  | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Treble%20Filter/RHA%20T10i%20Treble%20Filter.png)