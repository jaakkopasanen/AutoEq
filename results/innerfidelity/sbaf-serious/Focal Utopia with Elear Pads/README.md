# Focal Utopia with Elear Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.1; 54 -2.4; 60 -2.8; 66 -3.0; 72 -3.3; 79 -3.5; 87 -3.9; 96 -4.2; 106 -4.3; 116 -4.4; 128 -4.6; 141 -4.7; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.4; 302 -3.1; 332 -2.7; 365 -2.3; 402 -1.9; 442 -1.4; 486 -1.3; 535 -1.1; 588 -0.5; 647 -0.2; 712 -0.1; 783 0.1; 861 -0.1; 947 -0.1; 1042 0.2; 1146 -0.0; 1261 -0.1; 1387 -0.4; 1526 -0.6; 1678 -0.9; 1846 -0.4; 2031 -0.2; 2234 -0.7; 2457 -2.2; 2703 -2.4; 2973 -0.3; 3270 1.2; 3597 4.2; 3957 3.2; 4353 2.1; 4788 3.4; 5267 5.7; 5793 2.7; 6373 2.7; 7010 2.5; 7711 0.3; 8482 -2.1; 9330 -1.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia with Elear Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia with Elear Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 104 Hz   | 0.51 | -3.6 dB |
| Peaking | 219 Hz   | 0.92 | -2.2 dB |
| Peaking | 2610 Hz  | 4.11 | -3.0 dB |
| Peaking | 3679 Hz  | 5.69 | 4.4 dB  |
| Peaking | 5308 Hz  | 3.71 | 5.3 dB  |
| Peaking | 785 Hz   | 2.31 | 0.5 dB  |
| Peaking | 1628 Hz  | 6.78 | -0.8 dB |
| Peaking | 6797 Hz  | 9.79 | 2.7 dB  |
| Peaking | 8801 Hz  | 6.76 | -3.2 dB |
| Peaking | 18236 Hz | 4.54 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20with%20Elear%20Pads/Focal%20Utopia%20with%20Elear%20Pads.png)