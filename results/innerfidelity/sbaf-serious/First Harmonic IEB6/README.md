# First Harmonic IEB6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 0.0; 23 4.4; 25 3.8; 28 3.0; 31 2.3; 34 1.6; 37 1.0; 41 0.4; 45 -0.2; 49 -0.8; 54 -1.4; 60 -2.1; 66 -2.7; 72 -3.3; 79 -3.9; 87 -4.5; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.8; 141 -6.1; 155 -6.0; 170 -6.0; 187 -5.9; 206 -5.7; 227 -5.4; 249 -5.1; 274 -4.7; 302 -4.2; 332 -3.7; 365 -3.2; 402 -2.7; 442 -2.0; 486 -1.6; 535 -1.1; 588 -0.4; 647 0.1; 712 0.2; 783 0.7; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -2.6; 1678 -3.1; 1846 -3.3; 2031 -3.6; 2234 -4.1; 2457 -2.0; 2703 -3.7; 2973 -5.2; 3270 -4.6; 3597 -3.1; 3957 -2.7; 4353 -4.4; 4788 -5.7; 5267 -7.0; 5793 -10.9; 6373 -10.0; 7010 -4.9; 7711 -1.6; 8482 -0.1; 9330 0.0; 10263 -1.5; 11289 -3.0; 12418 -1.2; 13660 -1.0; 15026 -2.9; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`First Harmonic IEB6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `First Harmonic IEB6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.02 | 5.6 dB   |
| Peaking | 149 Hz   | 0.58 | -6.5 dB  |
| Peaking | 1897 Hz  | 2.43 | -3.2 dB  |
| Peaking | 3069 Hz  | 3    | -4.0 dB  |
| Peaking | 5919 Hz  | 3.07 | -11.5 dB |
| Peaking | 312 Hz   | 2.3  | -0.8 dB  |
| Peaking | 767 Hz   | 2.22 | 1.7 dB   |
| Peaking | 4570 Hz  | 9.01 | -1.3 dB  |
| Peaking | 8678 Hz  | 2.56 | 3.5 dB   |
| Peaking | 11257 Hz | 0.93 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/First%20Harmonic%20IEB6/First%20Harmonic%20IEB6.png)